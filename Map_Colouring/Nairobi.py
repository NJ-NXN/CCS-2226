import osmnx as ox
import matplotlib.pyplot as plt
import warnings

# Suppress minor warnings from the geographic downloader
warnings.filterwarnings('ignore')

# Nairobi Sub-Counties Map Coloring 
nairobi_neighbors = {
    "Westlands": ["Dagoretti North", "Starehe", "Mathare", "Kamukunji", "Langata"],
    "Dagoretti North": ["Westlands", "Dagoretti South", "Kibra", "Langata", "Starehe"],
    "Dagoretti South": ["Dagoretti North", "Kibra"],
    "Langata": ["Kibra", "Westlands", "Dagoretti North", "Starehe"],
    "Kibra": ["Langata", "Dagoretti North", "Dagoretti South"],
    "Roysambu": ["Kasarani", "Mathare", "Ruaraka"],
    "Kasarani": ["Roysambu", "Ruaraka", "Embakasi North"],
    "Ruaraka": ["Mathare", "Roysambu", "Kasarani", "Embakasi North"],
    "Starehe": ["Westlands", "Mathare", "Kamukunji", "Makadara", "Dagoretti North", "Langata"],
    "Mathare": ["Ruaraka", "Roysambu", "Starehe", "Kamukunji", "Westlands"],
    "Kamukunji": ["Starehe", "Mathare", "Makadara", "Westlands"],
    "Makadara": ["Kamukunji", "Starehe", "Embakasi West", "Embakasi South"],
    "Embakasi South": ["Makadara", "Embakasi East"],
    "Embakasi North": ["Kasarani", "Ruaraka", "Embakasi Central", "Embakasi West"],
    "Embakasi Central": ["Embakasi North", "Embakasi West", "Embakasi East"],
    "Embakasi East": ["Embakasi Central", "Embakasi South"],
    "Embakasi West": ["Embakasi North", "Embakasi Central", "Makadara"]
}

def greedy_coloring(graph):
    color_options = [1, 2, 3, 4, 5, 6] 
    assignment = {}
    sorted_nodes = sorted(graph.keys(), key=lambda node: len(graph[node]), reverse=True)
    for node in sorted_nodes:
        neighbor_colors = {assignment[neighbor] for neighbor in graph[node] if neighbor in assignment}
        for color in color_options:
            if color not in neighbor_colors:
                assignment[node] = color
                break
    return assignment

def draw_real_nairobi(solution_dict, total_colors): 
    integer_to_color = {1: "lightcoral", 2: "lightblue", 3: "lightgreen", 4: "gold", 5: "plum", 6: "orange"}
    gdfs = []

    # Fetch each sub-county individually to handle any potential OpenStreetMap naming mismatches
    for sc in solution_dict.keys():
        try:
            # We add "Constituency" as that is how OSM usually logs Kenyan sub-counties
            query = f"{sc}, Nairobi, Kenya"
            gdf = ox.geocode_to_gdf(query)
            # Map calculated color integer to an actual hex color
            color_int = solution_dict[sc]
            gdf['map_color'] = integer_to_color[color_int]
            gdfs.append(gdf)
        except Exception:
            print(f"  -> Note: Boundary for '{sc}' not found on OSM, skipping rendering for this specific area.")

    import pandas as pd
    if gdfs:
        # Combine all fetched regions into one map
        full_map = pd.concat(gdfs)
        
        fig, ax = plt.subplots(figsize=(12, 10))
        full_map.plot(ax=ax, color=full_map['map_color'], edgecolor='black', linewidth=1)
        
        ax.set_title(f"Nairobi Sub-Counties ({total_colors} Colors)", fontsize=16, fontweight="bold")
        ax.axis('off')
        plt.show()

if __name__ == "__main__":
    print("Running Greedy CSP Algorithm...")
    solution = greedy_coloring(nairobi_neighbors)
    total_colors_used = len(set(solution.values()))
    
    print(f"Minimum colors required: {total_colors_used}")
    draw_real_nairobi(solution, total_colors_used)