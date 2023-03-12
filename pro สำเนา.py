import networkx as nx
import matplotlib.pyplot as plt

def find_nearby_animals(animal, graph):
    neighbors = list(graph.neighbors(animal))
    for neighbor in neighbors:
        print(f"{animal} is connected to {neighbor} with weight {graph[animal][neighbor]['weight']}")
    
    if not neighbors:
        print(f"{animal} has no nearby animals.")

# find closest animal using BFS
def find_closest_animal(animal, graph):
    visited = {animal}
    queue = [(animal, 0)]
    
    while queue:
        current_animal, distance = queue.pop(0)
        
        if current_animal != animal:
            return current_animal, distance
        
        for neighbor in graph.neighbors(current_animal):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return None, None

#user input 
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

#directed graph
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
    
    if closest_animal is not None:
        f.write(f"\nThe closest animal to {animal} is {closest_animal} with a distance of {distance}.\n")
    else:
        f.write(f"No animals connected to {animal} were found.\n")
