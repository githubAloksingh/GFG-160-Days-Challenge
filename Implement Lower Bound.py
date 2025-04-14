#User function Template for python3
class Solution:
    def lowerBound(self, arr, target):
        #code here
        low=0
        high=len(arr)-1
        res=len(arr)
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]>=target:
                high=mid-1
                res=mid
            else:
                low=mid+1
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.lowerBound(A, D)
        print(ans)
        print("~")

# } Driver Code Ends
