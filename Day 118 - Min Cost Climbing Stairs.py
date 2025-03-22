#Back-end complete function Template for Python 3

class Solution:
    def __init__(self):
        self.dp=[-1]*100005
        
    def solve(self, cost, i):
        if i>=len(cost):
            return 0
        if self.dp[i]!=-1:
            return self.dp[i]
        one_step=cost[i]+self.solve(cost,i+1)
        two_step=cost[i]+self.solve(cost,i+2)
        self.dp[i]=min(one_step, two_step)
        return self.dp[i]
    def minCostClimbingStairs(self, cost):
        #Write your code here
        
        return min(self.solve(cost,0),self.solve(cost,1))
        


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends
