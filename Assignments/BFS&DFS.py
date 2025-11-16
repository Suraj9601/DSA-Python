def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    print("BFS Traversal:", " -> ".join(visited))


def dfs(matrix, start, visited, nodes):
    index = nodes.index(start)
    print(start, end=" ")
    visited[index] = True
    for i in range(len(matrix)):
        if matrix[index][i] == 1 and not visited[i]:
            dfs(matrix, nodes[i], visited, nodes)


nodes = ["A", "B", "C", "D", "E"]

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["B", "C"],
}

matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
]

while True:
    print("\n1. BFS Traversal")
    print("2. DFS Traversal")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        start = input("Enter starting node (A-E): ").upper()
        if start in graph:
            bfs(graph, start)
        else:
            print("Invalid node!")

    elif choice == "2":
        start = input("Enter starting node (A-E): ").upper()
        if start in nodes:
            visited = [False] * len(nodes)
            print("DFS Traversal:", end=" ")
            dfs(matrix, start, visited, nodes)
            print()
        else:
            print("Invalid node!")

    elif choice == "3":
        print("Program Ended.")
        break

    else:
        print("Invalid choice! Try again.")
