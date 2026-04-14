graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1, 4],
    4: [1, 3],
    5: [2],
    6: [2]
}
def dfs_path(node, dest, visited, path):
    visited.add(node)
    path.append(node)

    if node == dest:
        print("Path found:", " → ".join(map(str, path)))
        return True

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs_path(neighbor, dest, visited, path):
                return True

    # Backtracking
    path.pop()
    return False
visited = set()
source = 0
destination = 6

if not dfs_path(source, destination, visited, []):
    print("No path found")
    