import random

def clustering(size, no_of_clusters):
    new_arr = []
    for i in range(no_of_clusters):
        new_arr.append(random.sample(list(range(i*size, (i+1)*size)), size))
    print(new_arr)

# Driver Code
if __name__ == "__main__":
    size = 5
    no_of_clusters = 4
    clustering(size, no_of_clusters)
    
    
  
# A cluster preference template like 60% have the bias to a certain cluster.
# Randomisation within the clusters.
# Think of it like a political spectrum.
# a parameter for the clusters to show a bias in the population
# to check if the social choice functions returns one of the options.
# One for the cluster.
# One for the individual candidates option.