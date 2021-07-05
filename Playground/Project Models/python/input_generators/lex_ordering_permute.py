# Based off of https://www.geeksforgeeks.org/lexicographically-n-th-permutation-string/

# With changes to adapt to lists.
# Python3 program to print nth permutation.

# next_permutation method implementation.
def next_permutation(L):
    n = len(L)
    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1
  
    if i == -1:
        return False
  
    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1
  
    L[i], L[j] = L[j], L[i]
  
    left = i + 1
    right = n - 1
  
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
  
    return True
  
# Function to print nth permutation
# using next_permute()
def nPermute(string, n):
    string = list(string)
    new_string = []
  
    # Sort the string in lexicographically
    # ascending order
    string.sort()
    j = 2
  
    # Keep iterating until
    # we reach nth position
    while next_permutation(string):
        new_string = string
  
        # check for nth iteration
        if j == n:
            break
        j += 1
  
    # print string after nth iteration
    print(new_string)
  
# Driver Code
if __name__ == "__main__":
    noOfCandidates = 6
    string = list(range(noOfCandidates))
    n = 36
    nPermute(string, n)

# This code is contributed by
# sanjeev2552 and sid