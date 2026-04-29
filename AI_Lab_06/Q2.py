import heapq

graph = {
    'S': [('A', 3), ('B', 5)],
    'A': [('C', 4), ('D', 2)],
    'B': [('D', 6), ('G', 9)],
    'C': [('G', 7)],
    'D': [('E', 1)],
    'E': [('G', 3)],
    'G': []
}

h = {'S': 10, 'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 2, 'G': 0}

def best_first_route(start, goal):
    pq = [(h[start], start, [start], 0)]
    visited = set()

    while pq:
        _, node, path, cost = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Route:", " -> ".join(path))
            print("Total Cost:", cost)
            print("Cities explored:", len(visited))
            return

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (h[neighbor], neighbor, path + [neighbor], cost + weight))

best_first_route('S', 'G')