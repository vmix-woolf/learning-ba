import networkx as nx

DG = nx.DiGraph()
print(DG)
DG.add_edge("A", "B")
DG.add_edge("B", "A")
print(DG)

G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C")])
DG = nx.DiGraph(G)
print(DG)

DG = nx.DiGraph()
DG.add_edges_from([("A", "B"), ("B", "C")])
G = nx.Graph(DG)
print(G)

G = nx.Graph()
G.add_node(1)
G.add_node("A")
G.add_node("B")
G.add_node((2, 3))
G.add_edge("A", "B", weight=1.5)
G.add_edge(1, "F", weight=2.5, label="connection")
G.nodes[1]["color"] = "red"
print(G.nodes)

neighbors_of_A = G["A"]
edge_info = G["A"]["B"]
edge_weight = G["A"]["B"]["weight"]
print(neighbors_of_A, edge_info, edge_weight)
