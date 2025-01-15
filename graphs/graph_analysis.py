import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("A")
G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

num_nodes = G.number_of_nodes()  # 4
num_edges = G.number_of_edges()  # 4
is_connected = nx.is_connected(G)  # True
print(num_nodes)
print(num_edges)
print(is_connected)

degree_centrality = nx.degree_centrality(G)  # {'A': 0.6666666666666666, 'B': 1.0, 'C': 0.6666666666666666, 'D': 0.3333333333333333}
closeness_centrality = nx.closeness_centrality(G)  # {'A': 0.75, 'B': 1.0, 'C': 0.75, 'D': 0.6}
betweenness_centrality = nx.betweenness_centrality(G)  # {'A': 0.0, 'B': 0.6666666666666666, 'C': 0.0, 'D': 0.0}

import matplotlib.pyplot
G = nx.complete_graph(8)
pos = [[0, 1], [2, 3, 4, 5], [6, 7]]
pos = nx.shell_layout(G, pos)
options = {
    "node_color": "yellow",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}
nx.draw(G, pos, **options)
matplotlib.pyplot.show()

# Створення орієнтованого графа
G = nx.DiGraph()

# Додавання ребер
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 3), (4, 1)])

# Малювання графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)

plt.show()
