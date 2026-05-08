import matplotlib.pyplot as plt
import osmnx as ox

regions = ["Western Australia", "Northern Territory", "South Australia", "Queensland", "New South Wales"]
colors = ["Red", "Green", "Blue"]

neighbors = {
    "Western Australia": ["Northern Territory", "South Australia"],
    "Northern Territory": ["Western Australia", "South Australia", "Queensland"],
    "South Australia": ["Western Australia", "Northern Territory", "Queensland", "New South Wales"],
    "Queensland": ["Northern Territory", "South Australia", "New South Wales"],
    "New South Wales": ["Queensland", "South Australia"]
}

def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(regions):
        return assignment
    
    unassigned = [r for r in regions if r not in assignment]
    first_empty = unassigned[0]
    
    for color in colors:
        if is_valid(first_empty, color, assignment):
            assignment[first_empty] = color
            result = backtrack(assignment)
            if result is not None:
                return result
            del assignment[first_empty]
    return None

def draw_australia_map(solution_dict):
    #Draws the regions and their assigned colors in a pop-up window.
    #Fetch the exact boundaries for the states
    query = [f"{state}, Australia" for state in regions]
    gdf = ox.geocode_to_gdf(query)

    #Add the CSP solution colors to the map data
    gdf['color'] = gdf['display_name'].apply(
        lambda name: next(color for state, color in solution_dict.items() if state in name).lower()
    )
    #Plot the actual map
    fig, ax = plt.subplots(figsize=(10, 8))
    gdf.plot(ax=ax, color=gdf['color'], edgecolor='black', linewidth=1)
    
    ax.set_title("Australia Regions", fontsize=16, fontweight="bold")
    ax.axis('off') # Hide latitude/longitude axes
    plt.show()

if __name__ == "__main__":
    print("Running CSP Backtracking...")
    solution = backtrack({})
    if solution:
        for region, color in solution.items():
            print(f"- {region}: {color}")
        draw_australia_map(solution)