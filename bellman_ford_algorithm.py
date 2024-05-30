def bellman_ford(graph, start):
    # graph: { node: [(weight, neighbor), ...], ... }
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessor = {node: None for node in graph}

    for _ in range(len(graph) - 1):
        for node in graph:
            for weight, neighbor in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessor[neighbor] = node

    # Check for negative weight cycles
    for node in graph:
        for weight, neighbor in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative weight cycle")

    return distances, predecessor

# Örnek bir graf tanımlayalım (negatif ağırlıklı kenarlarla)
graph = {
    'A': [(1, 'B'), (4, 'C')],
    'B': [(1, 'A'), (2, 'C'), (5, 'D'), (4, 'E')],
    'C': [(4, 'A'), (2, 'B'), (1, 'D')],
    'D': [(5, 'B'), (1, 'C')],
    'E': [(4, 'B')]
}

start_node = 'A'
try:
    distances, predecessor = bellman_ford(graph, start_node)
    print("Shortest distances from", start_node, ":", distances)
    print("Predecessor:", predecessor)
except ValueError as e:
    print(e)
