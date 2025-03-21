class Solution:
    
    def solve(self, arr, i, n ,memo):
        if i>=n:
            return 0
        if i in memo:
            return memo[i]
        steal = arr[i]+self.solve(arr,i+2,n, memo)
        skip=self.solve(arr,i+1, n,memo)
        memo[i]=max(steal, skip)
        return memo[i]
    def findMaxSum(self,arr):
        # code here
        n=len(arr)
        memo={}

        return self.solve(arr, 0, n,memo)

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends
