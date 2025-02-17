#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        n=len(arr)
        l,r=0,n-1
        while l<=r:
            mid=l+(r-l)//2
            missing=arr[mid]-(mid+1)
            if missing<k:
                l=mid+1
            else:
                r=mid-1
        return l+k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends
