class Solution:
    
    def solve(self,arr, i, j,memo):
        if i==j:
            memo[i][j]=0
            return 0
        if memo[i][j]!=-1:
                return memo[i][j]
                
        mini=float('inf')
        for k in range(i,j):
            ans=self.solve(arr,i,k,memo)+self.solve(arr,k+1,j,memo)+arr[i-1]*arr[j]*arr[k]
            mini=min(ans,mini)
            memo[i][j]=mini
        return mini
    def matrixMultiplication(self, arr):
        # code here
        memo=[]
        n=len(arr)
        for _ in range(n):
            row=[]
            for _ in range(n):
                row.append(-1)
            memo.append(row)
        i=1
        j=n-1
        return self.solve(arr, i, j, memo)


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().matrixMultiplication(arr)  # find the missing number
    print(s)  # print the result
    print("~")

# } Driver Code Ends
