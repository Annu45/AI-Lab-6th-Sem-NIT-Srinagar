from queue import PriorityQueue

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

initial = (1, 2, 3,
           4, 0, 6,
           7, 5, 8)

moves = {
    "Up": -3,
    "Down": 3,
    "Left": -1,
    "Right": 1
}

def heuristic(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    possible = []

    if row > 0:
        possible.append(("Up", zero - 3))
    if row < 2:
        possible.append(("Down", zero + 3))
    if col > 0:
        possible.append(("Left", zero - 1))
    if col < 2:
        possible.append(("Right", zero + 1))

    for move, pos in possible:
        new_state = list(state)
        new_state[zero], new_state[pos] = new_state[pos], new_state[zero]
        neighbors.append((move, tuple(new_state)))

    return neighbors

pq = PriorityQueue()
pq.put((heuristic(initial), initial, []))

visited = set()

while not pq.empty():
    h, current, path = pq.get()

    if current in visited:
        continue

    visited.add(current)

    if current == goal:
        print("Initial:", initial, "h =", heuristic(initial))
        for i, (move, state) in enumerate(path, start=1):
            print(f"Move {i}: {move} -> {state} h={heuristic(state)}")
        print("\nGOAL REACHED")
        break

    for move, neighbor in get_neighbors(current):
        if neighbor not in visited:
            new_path = path + [(move, neighbor)]
            pq.put((heuristic(neighbor), neighbor, new_path))