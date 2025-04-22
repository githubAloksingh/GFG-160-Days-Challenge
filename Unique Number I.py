class Solution:
    def findUnique(self, arr):
        # code here
        freq={}
        for ch in arr:
            freq[ch]=freq.get(ch,0)+1
        for key, value in freq.items():
            if value==1:
                return key


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findUnique(arr)
        print(ans)
        print("~")
# } Driver Code Ends
