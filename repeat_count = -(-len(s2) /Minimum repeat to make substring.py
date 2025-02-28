#User function Template for python3
import math
class Solution:
    def minRepeats(self, s1, s2):
        # code here
        count= math.ceil(len(s2)/len(s1))
        
        repeated_string=count*s1
        if s2 in repeated_string:
            return count
        
        repeated_string+=s1
        if s2 in repeated_string:
            return count+1
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A, B))

# } Driver Code Ends
