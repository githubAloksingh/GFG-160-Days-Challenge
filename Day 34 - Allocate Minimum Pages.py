class Solution:
    #Function to find minimum number of pages.
    
    def isPossible(self, arr, k, maxPages):
        students=1
        pages=0
        for book in arr:
            if book+pages>maxPages:
                students+=1
                pages=book
                if students>k:
                    return False
            else:
                pages+=book
        return True
    def findPages(self, arr, k):
        #code here
        if k>len(arr):
            return -1
        low=max(arr)
        high=sum(arr)
        while low<=high:
            mid=low+(high-low)//2
            if self.isPossible(arr,k,mid):
                high=mid-1
            else:
                low=mid+1
        return low

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
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends
