import osmnx as ox
import networkx as nx
import numpy as np

def load_graph(city="Delhi, India"):
    """Download and prepare city graph with safety weights"""
    print(f"Loading {city} map...")
    G = ox.graph_from_place(city, network_type="walk")
    
    # Add safety weights
    for u, v, data in G.edges(data=True):
        crime_score = np.random.uniform(0, 1)
        lighting_score = np.random.uniform(0, 1)
        crowd_score = np.random.uniform(0, 1)
        data['safety_weight'] = round(
            (0.5 * crime_score) +
            (0.3 * (1 - lighting_score)) +
            (0.2 * (1 - crowd_score)), 4
        )
    
    print("Map ready! ✅")
    return G


def get_safest_route(start_lat, start_lon, end_lat, end_lon, G):
    """Find safest walking route between two coordinates"""
    
    # Find nearest intersection to given coordinates
    start_node = ox.nearest_nodes(G, start_lon, start_lat)
    end_node = ox.nearest_nodes(G, end_lon, end_lat)
    
    # Run Dijkstra algorithm
    safest_path = nx.dijkstra_path(G, start_node, end_node, weight='safety_weight')
    
    # Convert to coordinates
    coordinates = []
    for node in safest_path:
        lat = G.nodes[node]['y']
        lon = G.nodes[node]['x']
        coordinates.append({"lat": lat, "lon": lon})
    
    return {
        "start": {"lat": start_lat, "lon": start_lon},
        "end": {"lat": end_lat, "lon": end_lon},
        "total_stops": len(coordinates),
        "route": coordinates
    }


# Test karo
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