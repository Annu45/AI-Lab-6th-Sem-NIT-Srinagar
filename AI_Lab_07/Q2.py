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
heuristic = {
    'S': 10,
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 2,
    'G': 0
}
def astar(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, []))

    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        path = path + [node]

        print("Visited:", node)

        if node == goal:
            print("\nOptimal Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path)
                )

astar('S', 'G')