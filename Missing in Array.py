class Solution:
    def missingNum(self, arr):
        # code here
        arr.sort()
        st=set(arr)
        high=max(arr)
        for i in range(1,high+1):
            if i not in st:
                return i
        return i+1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNum(arr)
    print(s)

    print("~")
# } Driver Code Ends
