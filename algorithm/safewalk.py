import osmnx as ox
import networkx as nx
import numpy as np
import pandas as pd
from math import radians, sin, cos, sqrt, atan2

# Load crime data from CSV
safety_data = pd.read_csv("final_dataset.csv")

def get_crime_score(lat, lon):
    """Find nearest area and return its crime score"""
    min_dist = float('inf')
    nearest_crime = 5.0  # default if nothing found

    for _, row in safety_data.iterrows():
        # Calculate distance between road and area center
        dlat = radians(lat - row['lat'])
        dlon = radians(lon - row['lon'])
        a = sin(dlat/2)**2 + cos(radians(lat)) * cos(radians(row['lat'])) * sin(dlon/2)**2
        dist = 6371 * 2 * atan2(sqrt(a), sqrt(1-a))  # distance in km

        if dist < min_dist:
            min_dist = dist
            nearest_crime = row['crime_rate']

    return round(nearest_crime / 10.0, 4)  # normalize to 0-1


def get_crowd_score():
    """More people = safer. Based on time of day."""
    hour = pd.Timestamp.now().hour

    if 8 <= hour <= 11 or 17 <= hour <= 21:
        return 0.2   # rush hours - lots of people - safer
    elif 12 <= hour <= 16:
        return 0.5   # afternoon - medium
    else:
        return 0.8   # night - less people - unsafe


def load_graph(city="Delhi, India"):
    """Download city map and add safety score to every road"""
    print(f"Loading {city} map...")
    G = ox.graph_from_place(city, network_type="walk")

    for u, v, data in G.edges(data=True):
        # Get middle point of this road
        lat = (G.nodes[u]['y'] + G.nodes[v]['y']) / 2
        lon = (G.nodes[u]['x'] + G.nodes[v]['x']) / 2

        # Get all 3 scores
        crime_score = get_crime_score(lat, lon)
        crowd_score = get_crowd_score()

        # Lighting from OpenStreetMap
        lit = data.get('lit', 'no')
        if lit == 'yes':
            lighting_score = 1.0
        elif lit == 'limited':
            lighting_score = 0.5
        else:
            lighting_score = 0.0

        # Final safety weight — lower = safer
        data['safety_weight'] = round(
            (0.6 * crime_score) +
            (0.2 * (1 - lighting_score)) +
            (0.1 * crowd_score) +
            (0.1 * min(data.get('length', 100) / 500, 1.0)),
            4
        )

    print("Map ready! ✅")
    return G


def get_safest_route(start_lat, start_lon, end_lat, end_lon, G):
    """Given start and end coordinates, return the safest walking route"""

    start_node = ox.nearest_nodes(G, start_lon, start_lat)
    end_node = ox.nearest_nodes(G, end_lon, end_lat)

    safest_path = nx.dijkstra_path(G, start_node, end_node, weight='safety_weight')

    coordinates = []
    for node in safest_path:
        coordinates.append({
            "lat": G.nodes[node]['y'],
            "lon": G.nodes[node]['x']
        })

    return {
        "start": {"lat": start_lat, "lon": start_lon},
        "end": {"lat": end_lat, "lon": end_lon},
        "total_stops": len(coordinates),
        "route": coordinates
    }


# Test
if __name__ == "__main__":
    G = load_graph()

    result = get_safest_route(
        start_lat=28.5447, start_lon=77.1642,  # JNU
        end_lat=28.6139, end_lon=77.2090,       # Connaught Place
        G=G
    )

    print("\nRoute Found! ✅")
    print("Total stops:", result['total_stops'])
    print("First 3 coordinates:", result['route'][:3])