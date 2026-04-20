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

def detect_cycle(graph):
    visited = set()

    for start in graph:
        if start not in visited:
            queue = deque([(start, -1)])
            visited.add(start)

            while queue:
                node, parent = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, node))
                    elif neighbor != parent:
                        return True
    return False

if detect_cycle(graph):
    print("Cycle detected")
else:
    print("No cycle found")