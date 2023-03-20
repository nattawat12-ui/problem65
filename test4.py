import networkx as nx
import matplotlib.pyplot as plt

# Create an empty undirected graph
G = nx.Graph()

# Get user input for the genus
genus = input("Enter genus: ")

# Get user input for the number of animals in the genus
n = int(input("Enter the number of animals in the genus: "))

# Create a list to store the animal names
animals = []

# Add node to the graph
for i in range(n):
    animal = input(f"Enter the name of animal {i+1}: ")
    animals.append(animal)
    G.add_node(animal)

#relationships the animals and  weights
for i in range(n):
    for j in range(i+1, n):
        weight_str = input(f"Enter the weight of the relationship between {animals[i]} and {animals[j]}, or press enter to skip: ")
        if weight_str:
            try:
                weight = float(weight_str)
                G.add_edge(animals[i], animals[j], weight=weight)
            except ValueError:
                print("Invalid weight input. Skipping edge.")

# find the animal closest to a given animal
def find_farthest_animal(animal):
    neighbors = list(G.neighbors(animal))
    if not neighbors:
        return None
    
    # Find the maximum weight among neighbors
    max_weight = -float('inf')
    for neighbor in neighbors:
        if G[animal][neighbor]['weight'] > max_weight:
            max_weight = G[animal][neighbor]['weight']
    
    # Find all neighbors with maximum weight
    farthest_animals = [neighbor for neighbor in neighbors if G[animal][neighbor]['weight'] == max_weight]
    
    return farthest_animals


#input for the animal to find the closest animal for
target_animal = input("Enter the name of the animal to find the closest animal for: ")

closest_animals = find_farthest_animal(target_animal)

if closest_animals:
    print(f"The animal(s) closest to {target_animal} is {closest_animals}.")
else:
    print(f"{target_animal} has no neighbors.")

# Draw and display the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.savefig(f"{genus}.png")
plt.show()
