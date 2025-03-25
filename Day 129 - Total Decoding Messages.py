#User function Template for python3
class Solution:
    def __init__(self):
        self.t=[-1]*1001
        
    def solve(self, digits, i, n):
        if i==n:
            return 1
        if self.t[i]!=-1:
            return self.t[i]
        if digits[i]=='0':
            self.t[i]=0
            return 0
        result=self.solve(digits,i+1, n)
        if i+1<n:
            if digits[i]=='1' or (digits[i]=='2' and int(digits[i+1])<=6):
                result+=self.solve(digits,i+2,n)
        self.t[i]=result
        return result
        
	def countWays(self, digits):
		# Code here
		self.t=[-1]*1001
		n=len(digits)
		return self.solve(digits,0,n)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        digits = input()
        ob = Solution()
        ans = ob.countWays(digits)
        print(ans)
        print("~")

# } Driver Code Ends
