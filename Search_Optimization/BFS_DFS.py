# Define the Search Space (A Graph represented as an Adjacency List)
# This represents nodes connected to other nodes.
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

def bfs_path(graph, start, goal):
    """
    Breadth-First Search (BFS) to find the path from start to goal.
    Uses a Queue (First-In, First-Out) to explore neighbors level by level.
    """
    # Queue stores the paths. We initialize it with the starting node.
    queue = [[start]]
    # Set to keep track of visited nodes to avoid infinite loops
    visited = set()

    while queue:
        # Get the first path from the queue (FIFO behavior)
        path = queue.pop(0)
        # Get the last node from that path to check its neighbors
        node = path[-1]

        # If we reached the goal, return the path
        if node == goal:
            return path
        
        # If the node hasn't been visited, explore its neighbors
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                # Create a new path by adding the neighbor to the current path
                new_path = list(path)
                new_path.append(neighbor)
                # Add the new path to the back of the queue
                queue.append(new_path)
                
    return None # Return None if no path exists

def dfs_path(graph, start, goal):
    """
    Depth-First Search (DFS) to find the path from start to goal.
    Uses a Stack (Last-In, First-Out) to dive deep into a path before backtracking.
    """
    # Stack stores the paths. We initialize it with the starting node.
    stack = [[start]]
    # Set to keep track of visited nodes
    visited = set()

    while stack:
        # Get the last path from the stack (LIFO behavior)
        path = stack.pop()
        # Get the last node from that path
        node = path[-1]

        # If we reached the goal, return the path
        if node == goal:
            return path
        
        # If the node hasn't been visited, explore its neighbors
        if node not in visited:
            visited.add(node)
            # Reverse neighbors to explore them in alphabetical order (optional, but standardizes output)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    # Create a new path by adding the neighbor to the current path
                    new_path = list(path)
                    new_path.append(neighbor)
                    # Add the new path to the top of the stack
                    stack.append(new_path)
                    
    return None # Return None if no path exists

def main():
    print("Graph Search Algorithms")
    start_node = 'A'
    goal_node = 'H'
    
    print(f"\nSearching for path from '{start_node}' to '{goal_node}'\n")

    # Execute BFS
    bfs_result = bfs_path(graph, start_node, goal_node)
    print("1. Breadth-First Search (BFS):")
    if bfs_result:
        # Format the output using an arrow annotation
        print(f"Path found: {' -> '.join(bfs_result)}")
    else:
        print("No path found.")

    print("\n------------------------------------\n")

    # Execute DFS
    dfs_result = dfs_path(graph, start_node, goal_node)
    print("2. Depth-First Search (DFS):")
    if dfs_result:
        # Format the output using an arrow annotation
        print(f"Path found: {' -> '.join(dfs_result)}")
    else:
        print("No path found.")

if __name__ == "__main__":
    main()