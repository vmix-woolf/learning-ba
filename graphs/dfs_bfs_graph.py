import networkx as nx

# Створення графа
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

G = nx.Graph(graph)

# DFS
dfs_tree = nx.dfs_tree(G, source='A')
print(list(dfs_tree.edges()))  # виведе ребра DFS-дерева з коренем у вузлі A

# BFS
bfs_tree = nx.bfs_tree(G, source='A')
print(list(bfs_tree.edges()))  # виведе ребра BFS-дерева з коренем у вузлі A
