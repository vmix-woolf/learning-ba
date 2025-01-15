import networkx as nx

G = nx.Graph()
print(G)

G.add_node('A')
G.add_nodes_from(['B', 'C', 'D'])
print(G)

G.add_edge('A', 'B')
G.add_edges_from([('A', 'C'), ('B', 'C'), ('B', 'D')])
print(G)
print(G.nodes())
print(list(G.neighbors("A")))  # ['B', 'C']
print(G.edges())

G.remove_node('A')
print(G)
print(list(G.neighbors("B")))
G.remove_nodes_from(['B', 'C'])
print(G)