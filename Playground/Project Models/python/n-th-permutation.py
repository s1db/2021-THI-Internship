# Python3 program to print n-th permutation 
  
MAX_CHAR = 26
MAX_FACT = 20
fact = [None] * (MAX_FACT) 
  
# Utility for calculating factorials 
def precomputeFactorials(): 
  
    fact[0] = 1
    for i in range(1, MAX_FACT): 
        fact[i] = fact[i - 1] * i 
  
# Function for nth permutation 
def nPermute(string, n): 
  
    precomputeFactorials() 
  
    # length of given string 
    length = len(string) 
  
    # Count frequencies of all 
    # characters 
    freq = [0] * (MAX_CHAR) 
    for i in range(0, length): 
        freq[ord(string[i]) - ord('a')] += 1
  
    # out string for output string 
    out = [None] * (MAX_CHAR) 
  
    # iterate till sum equals n 
    Sum, k = 0, 0
  
    # We update both n and sum in 
    # this loop. 
    while Sum != n: 
  
        Sum = 0
          
        # check for characters present in freq[] 
        for i in range(0, MAX_CHAR): 
            if freq[i] == 0: 
                continue
  
            # Remove character 
            freq[i] -= 1
  
            # calculate sum after fixing 
            # a particuar char 
            xsum = fact[length - 1 - k] 
            for j in range(0, MAX_CHAR): 
                xsum = xsum // fact[freq[j]] 
            Sum += xsum 
  
            # if sum > n fix that char as 
            # present char and update sum 
            # and required nth after fixing 
            # char at that position 
            if Sum >= n: 
                out[k] = chr(i + ord('a')) 
                n -= Sum - xsum 
                k += 1
                break
              
            # if sum < n, add character back 
            if Sum < n: 
                freq[i] += 1
          
    # if sum == n means this char will provide 
    # its greatest permutation as nth permutation
    i = MAX_CHAR-1
    while k < length and i >= 0: 
        if freq[i]: 
            out[k] = chr(i + ord('a')) 
            freq[i] -= 1
            i += 1
            k += 1
          
        i -= 1
  
    # print result 
    print(''.join(out[:k])) 
  
# Driver Code
if __name__ == "__main__": 
  
    n = 69
    string = "geeksquiz"
  
    nPermute(string, n) 