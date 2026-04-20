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

def bfs_traversal(graph, start):
    visited = set()
    queue = deque([start])
    parent = {start: None}

    visited.add(start)

    print("BFS Order:", end=" ")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    print("\n\nBFS Tree (child : parent):")
    for node in parent:
        print(f"{node} : {parent[node]}")

bfs_traversal(graph, 0)