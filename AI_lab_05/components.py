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

def connected_components(graph):
    visited = set()

    for node in graph:
        if node not in visited:
            queue = deque([node])
            visited.add(node)
            component = []

            while queue:
                curr = queue.popleft()
                component.append(curr)

                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            print("Component:", component)

connected_components(graph)