# Program 2: Block World using Means-End Analysis
state = {
    "A": "table",
    "B": "table",
    "C": "table"
}
print("Initial State:")
print("A on table")
print("B on table")
print("C on table")
steps = []
# Step 1
steps.append("pickup(B)")
# Step 2
state["B"] = "A"
steps.append("stack(B, A)")
# Step 3
steps.append("pickup(C)")
# Step 4
state["C"] = "B"
steps.append("stack(C, B)")
print("\nGoal State:")
print("A on table")
print("B on A")
print("C on B")
print("\nSteps:")
for i, s in enumerate(steps, start=1):
    print(f"Step {i}: {s}")

print("\nGOAL Achieved")
print("Total moves:", len(steps))