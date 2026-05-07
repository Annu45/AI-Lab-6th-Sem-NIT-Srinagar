graph = {
    'A': [
        ('OR', ['B'], 1),
        ('AND', ['C', 'D'], 1)
    ],

    'B': [
        ('AND', ['E', 'F'], 1)
    ],

    'C': [],
    'D': [],
    'E': [],
    'F': []
}
heuristic = {
    'A': 0,
    'B': 5,
    'C': 3,
    'D': 4,
    'E': 7,
    'F': 9
}
def ao_star(node):
    if graph[node] == []:
        return 0

    costs = []

    for connector_type, children, edge_cost in graph[node]:

        total = 0

        for child in children:
            total += edge_cost + ao_star(child)

        costs.append((total, connector_type, children))

    best = min(costs, key=lambda x: x[0])

    return best[0]

print("Total Minimum Cost from A:", ao_star('A'))