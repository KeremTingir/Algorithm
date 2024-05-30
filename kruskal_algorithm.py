class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    # graph: [(weight, node1, node2), ...]
    mst = []
    uf = UnionFind({node for edge in graph for node in edge[1:]})

    graph.sort()  # Sort edges by weight

    for weight, node1, node2 in graph:
        if uf.find(node1) != uf.find(node2):
            uf.union(node1, node2)
            mst.append((node1, node2, weight))
    
    return mst

# Örnek bir graf tanımlayalım (kenar listesi formatında)
edges = [
    (1, 'A', 'B'),
    (3, 'A', 'C'),
    (3, 'B', 'C'),
    (1, 'B', 'D'),
    (1, 'C', 'D')
]

mst = kruskal(edges)
print("Minimum Spanning Tree (Kruskal):", mst)
