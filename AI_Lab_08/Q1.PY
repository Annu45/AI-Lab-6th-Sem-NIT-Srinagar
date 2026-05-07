# Program 1: Robot Traversal using Means-End Analysis
current = [0, 0]
goal = [3, 3]
step = 1
print(f"Initial: ({current[0]},{current[1]}) Goal: ({goal[0]},{goal[1]}) diff: {goal[0]-current[0]},{goal[1]-current[1]}")
while current != goal:

    dx = goal[0] - current[0]
    dy = goal[1] - current[1]

    if dx > 0:
        current[0] += 1
        move = "MoveRight"

    elif dx < 0:
        current[0] -= 1
        move = "MoveLeft"

    elif dy > 0:
        current[1] += 1
        move = "MoveUp"

    elif dy < 0:
        current[1] -= 1
        move = "MoveDown"

    print(f"Step {step}: {move} -> ({current[0]},{current[1]}) diff: {goal[0]-current[0]},{goal[1]-current[1]}")

    step += 1
print("GOAL Reached")
print("Total moves:", step - 1)