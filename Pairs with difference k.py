#User function Template for python3
class Solution:
	def countPairs(self, arr, k):
    	# code here
    	n=len(arr)
    	cnt=0
    	freq={}
    	for i in range(n):
    	    if (arr[i]+k) in freq:
    	        cnt+=freq[arr[i]+k]
    	    if (arr[i]-k) in freq:
    	        cnt+=freq[arr[i]-k]
	        freq[arr[i]]=freq.get(arr[i],0)+1
	    return cnt



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairs(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends
