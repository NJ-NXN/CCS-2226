import heapq

def a_star_search(graph, start, goal, heuristics):
    """
    A* Search Algorithm implementation.
    graph: Adjacency list representing the graph with step costs.
    start: The starting node.
    goal: The target node.
    heuristics: A dictionary mapping nodes to their estimated cost to the goal.
    """
    # Priority queue stores (f_cost, current_node, path)
    open_set = []
    heapq.heappush(open_set, (0 + heuristics[start], start, [start]))
    
    # Dictionary to keep track of the lowest g_cost to a specific node
    g_costs = {start: 0}
    
    while open_set:
        # Pop the node with the lowest f(n)
        current_f, current_node, path = heapq.heappop(open_set)
        
        # If we reached the goal, return the optimized path and cost
        if current_node == goal:
            return path, g_costs[current_node]
            
        # Explore neighbors
        for neighbor, step_cost in graph.get(current_node, {}).items():
            # Calculate exact cost from start to this neighbor
            tentative_g_cost = g_costs[current_node] + step_cost
            
            # If this is a cheaper path to the neighbor, process it
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristics[neighbor]
                
                # Add the neighbor and its path to the priority queue
                new_path = path + [neighbor]
                heapq.heappush(open_set, (f_cost, neighbor, new_path))
                
    return None, float('inf') # Return if no path exists