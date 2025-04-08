from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code her
        n=len(prices)
        lmin=prices[0]
        lmax=prices[0]
        i=0
        res=0
        while i<n-1:
            while i<n-1 and prices[i]>=prices[i+1]:
                i+=1
            lmin=prices[i]
            while i<n-1 and prices[i]<=prices[i+1]:
                i+=1
            lmax=prices[i]
            res+=(lmax-lmin)
        return res
            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)
        print("~")

# } Driver Code Ends
