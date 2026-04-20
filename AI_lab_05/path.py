graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1, 4],
    4: [1, 3],
    5: [2],
    6: [2]
}
from collections import deque

def bfs_path(graph, start, end):
    visited = set()
    queue = deque([start])
    parent = {start: None}

    visited.add(start)

    while queue:
        node = queue.popleft()

        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    return None

path = bfs_path(graph, 0, 6)

if path:
    print("Shortest Path:", " → ".join(map(str, path)))
else:
    print("No path found")