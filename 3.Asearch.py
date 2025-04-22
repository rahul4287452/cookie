def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])  # Nodes yet to be evaluated
    closed_set = set()  # Nodes that have already been evaluated
    g = {}  # Store distance from starting node to each node
    parents = {}  # Map each node to its parent for path reconstruction

    g[start_node] = 0  # Distance from the start node to itself is zero
    parents[start_node] = start_node  # The start node is its own parent (no parent initially)

    while len(open_set) > 0:
        n = None  # Node with the lowest f() score will be selected

        # Find the node in open_set with the lowest f(n)
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node:  # If the current node is the stop node, path is found
            path = []  # Reconstruct the path from the start node to the stop node
            total_cost = g[n]  # This stores the total cost of the path

            while parents[n] != n:  # Backtrack to the start node
                path.append(n)
                n = parents[n]
            path.append(start_node)  # Add the start node to the path
            path.reverse()  # Reverse the path to get it from start to stop

            # Print the results
            print('Path found: {}'.format(path))
            print('Total cost of the path: {}'.format(total_cost))
            return path

        # If no path is found, terminate
        if n is None:
            print('Path does not exist!')
            return None

        # Remove node n from open_set and add it to closed_set
        open_set.remove(n)
        closed_set.add(n)

        # Process each neighbor of the current node
        for (m, weight) in get_neighbors(n):
            if m in closed_set:  # If node m is already evaluated, skip it
                continue

            tentative_g = g[n] + weight  # Calculate the tentative g value (cost from start to m)

            if m not in open_set:  # If m is not in open_set, add it
                open_set.add(m)
            elif tentative_g >= g[m]:  # If the new path is not better, skip it
                continue

            # If this path to m is better, update g and parent
            parents[m] = n
            g[m] = tentative_g

    print('Path does not exist!')  # If open_set is empty, no path was found
    return None


# Define the function to return the neighbors and their distances for a given node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]  # List of neighbors and edge weights
    else:
        return []

# Define heuristic distances for each node
def heuristic(n):
    H_dist = {
        'S': 5,
        'A': 3,
        'B': 4,
        'C': 2,
        'D': 6,
        'G': 0,
    }
    return H_dist.get(n, float('inf'))  # Default to infinity if node not found in H_dist

# Define the graph structure with nodes and edges (neighbors with their respective weights)
Graph_nodes = {
    'S': [('A', 1), ('G', 10)],  # Start node has edges to A and G with weights 1 and 10
    'A': [('B', 2), ('C', 1)],  # A has edges to B and C with weights 2 and 1
    'B': [('D', 5)],  # B has an edge to D with weight 5
    'C': [('D', 3), ('G', 4)],  # C has edges to D and G with weights 3 and 4
    'D': [('G', 2)],  # D has an edge to G with weight 2
}

# Call the A* algorithm with the start node 'S' and goal node 'G'
aStarAlgo('S', 'G')