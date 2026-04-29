import heapq
capacity1 = 4
capacity2 = 3
goal = 2
def heuristic(state):
    return abs(goal - state[0])  # based on 4L jug
def get_neighbors(state):
    x, y = state
    neighbors = []
    # Fill
    neighbors.append((capacity1, y))
    neighbors.append((x, capacity2))
    # Empty
    neighbors.append((0, y))
    neighbors.append((x, 0))
    # Pour
    transfer = min(x, capacity2 - y)
    neighbors.append((x - transfer, y + transfer))
    transfer = min(y, capacity1 - x)
    neighbors.append((x + transfer, y - transfer))
    return neighbors
def best_first_jug():
    start = (0, 0)
    pq = [(heuristic(start), start, [start])]
    visited = set()
    while pq:
        _, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        if state[0] == goal:
            print("Solution Path:")
            for p in path:
                print(p)
            return

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic(neighbor), neighbor, path + [neighbor]))

best_first_jug()