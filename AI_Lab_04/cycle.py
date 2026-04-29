graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1, 4],
    4: [1, 3],
    5: [2],
    6: [2]
}
def dfs_cycle(node, visited, parent):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs_cycle(neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True

    return False

visited = set()

if dfs_cycle(0, visited, -1):
    print("Cycle detected")
else:
    print("No cycle found")