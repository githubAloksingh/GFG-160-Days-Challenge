#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		n=len(arr)
		maxi=float('-inf')
		prefix, suffix=1,1
		for i in range(n):
		    if prefix==0:
		        prefix = 1
		    if suffix ==0:
		        suffix=1
		    prefix*=arr[i]
		    suffix*=arr[n-i-1]
		    maxi=max(maxi,max(prefix, suffix))
	    return maxi
		    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
