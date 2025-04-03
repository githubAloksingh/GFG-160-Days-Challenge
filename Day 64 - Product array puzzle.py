#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n=len(arr)
        prefix=[1]*n
        suffix=[1]*n
        res=[1]*n
        for i in range(1,n):
            prefix[i]=arr[i-1]*prefix[i-1]
        for i in range(n-2, -1,-1):
            suffix[i]=arr[i+1]*suffix[i+1]
        for i in range(n):
            res[i]=prefix[i]*suffix[i]
        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends
