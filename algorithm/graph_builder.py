import osmnx as ox
import networkx as nx
import numpy as np

# Download Delhi street map
print("Downloading Delhi map... please wait ⏳")
G = ox.graph_from_place("Delhi, India", network_type="walk")
print("Graph created! ✅")

# Add safety weights to every edge (road)
print("Adding safety weights to roads...")

for u, v, data in G.edges(data=True):
    # Mock safety scores (0 to 1) — will be replaced by real data later
    crime_score = np.random.uniform(0, 1)      # 0 = safe, 1 = dangerous
    lighting_score = np.random.uniform(0, 1)   # 0 = dark, 1 = well lit
    crowd_score = np.random.uniform(0, 1)      # 0 = empty, 1 = crowded

    # Safety weight formula
    # Higher weight = more dangerous = avoid this road
    safety_weight = (0.5 * crime_score) + (0.3 * (1 - lighting_score)) + (0.2 * (1 - crowd_score))

    data['safety_weight'] = round(safety_weight, 4)

print("Safety weights added! ✅")
print("Sample edge data:", list(G.edges(data=True))[0])

# Find safest path between two points
print("\nFinding safest path...")

# Pick any two random nodes from Delhi map
all_nodes = list(G.nodes)
start_node = all_nodes[0]
end_node = all_nodes[100]

# Dijkstra algorithm — finds path with lowest safety_weight
safest_path = nx.dijkstra_path(G, start_node, end_node, weight='safety_weight')

print("Start Node:", start_node)
print("End Node:", end_node)
print("Safest Path (node IDs):", safest_path)
print("Total nodes in path:", len(safest_path))



# Convert node IDs to coordinates
print("\nConverting nodes to coordinates...")

coordinates = []
for node in safest_path:
    lat = G.nodes[node]['y']   # latitude
    lon = G.nodes[node]['x']   # longitude
    coordinates.append((lat, lon))

print("Coordinates of safest path:")
for i, coord in enumerate(coordinates[:5]):  # show first 5 only
    print(f"  Stop {i+1}: lat={coord[0]:.6f}, lon={coord[1]:.6f}")

print(f"  ... and {len(coordinates)-5} more stops")
print("\nTotal coordinates:", len(coordinates))