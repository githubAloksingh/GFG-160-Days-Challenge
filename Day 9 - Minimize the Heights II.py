class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n=len(arr)
        if n==1:
            return 0
        arr.sort()
        ans=arr[-1]-arr[0]
       
        for i in range(1,n):
            if arr[i]-k<0:
                continue
            min_val=min(arr[0]+k, arr[i]-k)
            max_val=max(arr[-1]-k, arr[i-1]+k)
            ans=min(ans, max_val-min_val)
        return ans
        #User function Template for python3



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends
