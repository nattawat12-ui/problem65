import networkx as nx
import matplotlib.pyplot as plt

def find_nearby_animals(animal, graph):
    neighbors = list(graph.neighbors(animal))
    for neighbor in neighbors:
        print(f"{animal} is connected to {neighbor} with weight {graph[animal][neighbor]['weight']}")
    
    if not neighbors:
        print(f"{animal} has no nearby animals.")

# find closest animal BFS
def find_closest_animal(animal, graph):
    visited = {animal}
    queue = [(animal, 0)]
    closest_animal = None
    min_weight = float('inf')
    
    while queue:
        current_animal, distance = queue.pop(0)
        
        if current_animal != animal and graph[animal][current_animal]['weight'] < min_weight:
            closest_animal = current_animal
            min_weight = graph[animal][current_animal]['weight']
        
        for neighbor in graph.neighbors(current_animal):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + graph[current_animal][neighbor]['weight']))
    
    return closest_animal, min_weight


# function to save 
def save_data(data, filepath):
    with open(filepath, "a") as f:
        for animal, relationships in data.items():
            for neighbor, weight in relationships.items():
                f.write(f"{animal} is connected to {neighbor} with weight {weight}\n")

# user input 
num_animals = int(input("Enter the number of animals: "))
data = {}
for i in range(num_animals):
    animal = input("Enter the animal name: ")
    num_relationships = int(input(f"Enter the number of relationships for {animal}: "))
    relationships = {}
    for j in range(num_relationships):
        relationship = input(f"Enter the name of the {j+1} relationship: ")
        weight = float(input(f"Enter the weight of the {j+1} relationship: "))
        relationships[relationship] = weight
    data[animal] = relationships

# save user input 
filepath = "user_input.txt"
save_data(data, filepath)

# directed graph
G = nx.DiGraph()

# Add nodes and edges to graph
for animal in data.keys():
    G.add_node(animal)
    relationships = data[animal]
    for neighbor, weight in relationships.items():
        G.add_edge(animal, neighbor, weight=weight)

# Draw the graph
pos = nx.circular_layout(G)
nx.draw_networkx(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.show()

animal = input("Enter an animal to find its nearby animals: ")
find_nearby_animals(animal, G)

animal = input("Enter an animal to find the closest animal: ")
closest_animal, distance = find_closest_animal(animal, G)

with open("output.txt", "w") as f:
    f.write(f"Nearby animals for {animal}:\n")
    neighbors = list(G.neighbors(animal))
    if not neighbors:
        f.write(f"{animal} has no nearby animals.\n")
    else:
        for neighbor in neighbors:
            f.write(f"{animal} is connected to {neighbor} with weight {G[animal][neighbor]['weight']}\n")
    
    f.write(f"\nClosest animal to {animal} is {closest_animal} at a distance of {distance}.\n")
