import heapq
class Solution:
	def kLargest(self, arr, k):
		# Your code here
		min_heap=[]
		for num in arr:
		    heapq.heappush(min_heap, num)
		    
		    if len(min_heap)>k:
		        heapq.heappop(min_heap)
        return sorted(min_heap, reverse=True)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.kLargest(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends
