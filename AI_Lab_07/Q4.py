from collections import deque
import heapq
graph = {
    'S': [('A', 3), ('B', 5)],
    'A': [('C', 4), ('D', 2)],
    'B': [('D', 6), ('G', 9)],
    'C': [('G', 7)],
    'D': [('E', 1)],
    'E': [('G', 3)],
    'G': []
}
heuristic = {
    'S': 10,
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 2,
    'G': 0
}
# DFS
def dfs(start, goal):
    stack = [(start, [start], 0)]
    visited = set()

    while stack:
        node, path, cost = stack.pop()

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, w in reversed(graph[node]):
                stack.append((neighbor, path + [neighbor], cost + w))
# BFS
def bfs(start, goal):
    q = deque([(start, [start], 0)])
    visited = set()

    while q:
        node, path, cost = q.popleft()

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, w in graph[node]:
                q.append((neighbor, path + [neighbor], cost + w))

# Best First Search
def best_first(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], start, [start], 0))

    visited = set()

    while pq:
        h, node, path, cost = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, w in graph[node]:
                heapq.heappush(
                    pq,
                    (heuristic[neighbor],
                     neighbor,
                     path + [neighbor],
                     cost + w)
                )

# A*
def astar(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, [start]))

    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return path, g

        if node not in visited:
            visited.add(node)

            for neighbor, w in graph[node]:
                new_g = g + w
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    pq,
                    (new_f,
                     new_g,
                     neighbor,
                     path + [neighbor])
                )

print("DFS:", dfs('S', 'G'))
print("BFS:", bfs('S', 'G'))
print("Best First:", best_first('S', 'G'))
print("A*:", astar('S', 'G'))