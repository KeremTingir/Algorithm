import heapq

def dijkstra(graph, start):
    # graph: { node: [(weight, neighbor), ...], ... }
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, node)
    shortest_path_tree = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue

        for weight, neighbor in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_path_tree[neighbor] = current_node

    return distances, shortest_path_tree

# Örnek bir graf tanımlayalım
graph = {
    'A': [(1, 'B'), (4, 'C')],
    'B': [(1, 'A'), (2, 'C'), (5, 'D')],
    'C': [(4, 'A'), (2, 'B'), (1, 'D')],
    'D': [(5, 'B'), (1, 'C')]
}

start_node = 'A'
distances, shortest_path_tree = dijkstra(graph, start_node)
print("Shortest distances from", start_node, ":", distances)
print("Shortest path tree:", shortest_path_tree)
