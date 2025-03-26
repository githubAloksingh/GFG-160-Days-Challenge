from collections import defaultdict
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        xr=0
        n=len(arr)
        mpp=defaultdict(int)
        mpp[xr]=1
        cnt=0
        for i in range(n):
            xr=xr^arr[i]
            x=xr^k
            cnt+=mpp[x]
            mpp[xr]+=1
        return cnt

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends
