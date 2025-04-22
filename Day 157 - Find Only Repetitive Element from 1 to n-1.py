#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        #code here
        freq={}
        for ch in arr:
            freq[ch]=freq.get(ch,0)+1
        for key,value in freq.items():
            if value>1:
                return key
                
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        print(ob.findDuplicate(arr))
        print("~")

# } Driver Code Ends
