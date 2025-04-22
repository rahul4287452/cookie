graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['E', 'G'],
    'G': ['F']
}

# DFS function
def dfs(node, visited=None):
    # Initialize visited set if not provided
    if visited is None:
        visited = set()
    # Print current node if not visited
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
    # Recursive call for all adjacent nodes
    for neighbor in graph[node]:
        if neighbor not in visited:  # Make sure we visit a node only once
            dfs(neighbor, visited)

# Driver code
if __name__ == "__main__":
    dfs('A')
