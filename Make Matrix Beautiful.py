#User function Template for python3

class Solution:
    def findMinOperation(self, mat):
        # code here
        n=len(mat)
        res=0
        max_sum=0
        for i in range(n):
            sum=0
            for j in range(n):
                sum+=mat[i][j]
            max_sum=max(max_sum,sum)
        for j in range(n):
            sum=0
            for i in range(n):
                sum+=mat[i][j]
            max_sum=max_sum=max(max_sum,sum)
        for i in range(n):
            sum=0
            for j in range(n):
                sum+=mat[i][j]
            res+=(max_sum-sum)
        return res
                
            

#{ 
 # Driver Code Starts
# Driver code
t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    sol = Solution()
    print(sol.findMinOperation(matrix))
    print("~")
# } Driver Code Ends
