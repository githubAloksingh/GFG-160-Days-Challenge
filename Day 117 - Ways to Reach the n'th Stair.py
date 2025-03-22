
class Solution:
    def __init__(self):
        self.memo=[-1]*45
    def solve(self, n):
        if n<=1:
            return 1
        if self.memo[n]!=-1:
            return self.memo[n]
        self.memo[n]=self.solve(n-1)+self.solve(n-2)
        return self.memo[n]
    def countWays(self, n):
        # code here
        return self.solve(n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

        print("~")

# } Driver Code Ends
