import random

def clustering(size, no_of_clusters):
    new_arr = []
    for i in range(no_of_clusters):
        new_arr.append(random.sample(list(range(i*size, (i+1)*size)), size))
    print(random.sample(new_arr, size))

# Driver Code
if __name__ == "__main__":
    size = 3
    no_of_clusters = 3
    clustering(size, no_of_clusters)