import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from safewalk import load_graph, get_safest_route

# Load graph once
G = load_graph()

# Test routes — famous Delhi locations
test_cases = [
    {
        "name": "JNU to Connaught Place",
        "start_lat": 28.5447, "start_lon": 77.1642,
        "end_lat": 28.6139, "end_lon": 77.2090
    },
    {
        "name": "Lajpat Nagar to Saket Metro",
        "start_lat": 28.5677, "start_lon": 77.2431,
        "end_lat": 28.5245, "end_lon": 77.2066
    },
    {
        "name": "Rohini to Pitampura",
        "start_lat": 28.7041, "start_lon": 77.1025,
        "end_lat": 28.7033, "end_lon": 77.1322
    }
]

# Test each route
for test in test_cases:
    print(f"\nTesting: {test['name']}")
    print("-" * 40)

    result = get_safest_route(
        test['start_lat'], test['start_lon'],
        test['end_lat'], test['end_lon'],
        G
    )

    # Calculate total distance
    total_dist = 0
    coords = result['route']
    for i in range(len(coords) - 1):
        lat1, lon1 = coords[i]['lat'], coords[i]['lon']
        lat2, lon2 = coords[i+1]['lat'], coords[i+1]['lon']
        # Approximate distance in meters
        dist = ((lat2-lat1)**2 + (lon2-lon1)**2) ** 0.5 * 111000
        total_dist += dist

    print(f"Total stops: {result['total_stops']}")
    print(f"Approx distance: {round(total_dist/1000, 2)} km")
    print(f"Start: {coords[0]}")
    print(f"End: {coords[-1]}")

    # Visualize
    start_node = ox.nearest_nodes(G, test['start_lon'], test['start_lat'])
    end_node = ox.nearest_nodes(G, test['end_lon'], test['end_lat'])
    path = nx.dijkstra_path(G, start_node, end_node, weight='safety_weight')

    fig, ax = ox.plot_graph_route(
    G, path,
    route_color='green',
    route_linewidth=3,
    node_size=0,
    bgcolor='black',
    show=False,
    save=True,
    filepath=f"{test['name'].replace(' ', '_')}.png"
    )
    plt.close()
    print(f"Map saved! ✅")

print("\nAll tests done! ✅")