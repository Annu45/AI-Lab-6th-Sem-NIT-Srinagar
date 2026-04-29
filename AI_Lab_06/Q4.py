import heapq
def is_valid(m, c):
    return (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)
def heuristic(state):
    m, c, _ = state
    return m + c  # people left
def get_neighbors(state):
    m, c, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    neighbors = []

    for dm, dc in moves:
        if boat == 'L':
            new_m, new_c = m - dm, c - dc
            new_boat = 'R'
        else:
            new_m, new_c = m + dm, c + dc
            new_boat = 'L'

        if 0 <= new_m <= 3 and 0 <= new_c <= 3 and is_valid(new_m, new_c):
            neighbors.append((new_m, new_c, new_boat))

    return neighbors
def best_first_mc():
    start = (3, 3, 'L')
    goal = (0, 0, 'R')
    pq = [(heuristic(start), start, [start])]
    visited = set()

    while pq:
        _, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            print("Solution Path:")
            for p in path:
                print(p)
            return

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic(neighbor), neighbor, path + [neighbor]))

best_first_mc()
