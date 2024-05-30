import heapq

def prim(graph):
    # graph: { node: [(weight, neighbor), ...], ... }
    mst = []  # Minimum spanning tree
    visited = set()
    min_heap = [(0, None, list(graph.keys())[0])]  # (weight, from_node, to_node)

    while min_heap:
        weight, frm, to = heapq.heappop(min_heap)
        if to not in visited:
            visited.add(to)
            if frm is not None:
                mst.append((frm, to, weight))
            
            for edge_weight, neighbor in graph[to]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, to, neighbor))
    
    return mst

# Örnek bir graf tanımlayalım
graph = {
    'A': [(1, 'B'), (3, 'C')],
    'B': [(1, 'A'), (3, 'C'), (1, 'D')],
    'C': [(3, 'A'), (3, 'B'), (1, 'D')],
    'D': [(1, 'B'), (1, 'C')]
}

mst = prim(graph)
print("Minimum Spanning Tree (Prim):", mst)
