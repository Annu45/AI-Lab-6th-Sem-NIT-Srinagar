# Program 3: TSP using Brute Force
from itertools import permutations
cities = ['A', 'B', 'C', 'D']
dist = {
    ('A', 'B'): 1,
    ('A', 'C'): 4,
    ('A', 'D'): 4,
    ('B', 'A'): 1,
    ('B', 'C'): 5,
    ('B', 'D'): 1,
    ('C', 'A'): 4,
    ('C', 'B'): 5,
    ('C', 'D'): 9,
    ('D', 'A'): 4,
    ('D', 'B'): 1,
    ('D', 'C'): 9
}
min_cost = float('inf')
best_path = None
print("Tours from A:\n")
for perm in permutations(cities[1:]):
    path = ['A'] + list(perm) + ['A']
    cost = 0
    for i in range(len(path)-1):
        cost += dist[(path[i], path[i+1])]
    print(" -> ".join(path), ":", cost)
    if cost < min_cost:
        min_cost = cost
        best_path = path
print("\nOptimal Tour:")
print(" -> ".join(best_path))
print("Optimal Cost:", min_cost)