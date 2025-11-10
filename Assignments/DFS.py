# DFS using Adjacency Matrix

graph = [
    [0, 1, 1, 0, 0],  # A
    [1, 0, 0, 1, 1],  # B
    [1, 0, 0, 0, 0],  # C
    [0, 1, 0, 0, 0],  # D
    [0, 1, 0, 0, 0]   # E
]

visited = [False] * 5
nodes = ['A', 'B', 'C', 'D', 'E']

def dfs(start):
    print(nodes[start], end=" ")
    visited[start] = True
    for i in range(5):
        if graph[start][i] == 1 and not visited[i]:
            dfs(i)

print("DFS Traversal starting from A:")
dfs(0)
print()

# BFS using Adjacency List

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                if n not in visited:
                    queue.append(n)
    print(" -> ".join(visited))

print("BFS Traversal starting from A:")
bfs('A')
