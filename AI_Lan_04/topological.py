dag = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [4],
    4: [],
    5: [],
    6: []
}
def dfs_topo(node, visited, stack):
    visited.add(node)

    for neighbor in dag[node]:
        if neighbor not in visited:
            dfs_topo(neighbor, visited, stack)

    stack.append(node)

visited = set()
stack = []

for node in dag:
    if node not in visited:
        dfs_topo(node, visited, stack)

print("Topological Order:")
print(stack[::-1])   # reverse
