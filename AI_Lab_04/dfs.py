graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1, 4],
    4: [1, 3],
    5: [2],
    6: [2]
}
def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

visited = set()
print("DFS Order:")
dfs(0, visited)
