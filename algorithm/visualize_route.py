import osmnx as ox
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Download Delhi map
print("Downloading Delhi map... ⏳")
G = ox.graph_from_place("Delhi, India", network_type="walk")

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

# Find safest path
all_nodes = list(G.nodes)
start_node = all_nodes[0]
end_node = all_nodes[100]
safest_path = nx.dijkstra_path(G, start_node, end_node, weight='safety_weight')

# Draw the map with route
print("Drawing map... 🗺️")
fig, ax = ox.plot_graph_route(
    G, 
    safest_path,
    route_color='green',
    route_linewidth=3,
    node_size=0,
    bgcolor='black',
    show=True
)

print("Map drawn! ✅")