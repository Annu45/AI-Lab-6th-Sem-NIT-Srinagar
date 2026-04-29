import heapq
# Graph with costs
graph = {
    'S': [('A', 3), ('B', 5)],
    'A': [('S', 3), ('C', 4), ('D', 2)],
    'B': [('S', 5), ('D', 6), ('G', 9)],
    'C': [('A', 4), ('G', 7)],
    'D': [('A', 2), ('B', 6), ('E', 1)],
    'E': [('D', 1), ('G', 3)],
    'G': []
}
# Heuristic values
h = {'S': 10, 'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 2, 'G': 0}

def best_first_search(start, goal):
    visited = set()
    pq = [(h[start], start, [start], 0)]  # (heuristic, node, path, cost)

    while pq:
        _, node, path, cost = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        print(node, end=" ")

        if node == goal:
            print("\nPath:", " -> ".join(path))
            print("Total Cost:", cost)
            return

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (h[neighbor], neighbor, path + [neighbor], cost + weight))

best_first_search('S', 'G')