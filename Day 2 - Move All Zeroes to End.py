#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	non_zeros=[]
    	for num in arr:
    	    if num!=0:
    	        non_zeros.append(num)
    	 
	    zero_count=len(arr)-len(non_zeros)
    	zeros=[0]*zero_count
    	arr[:]=non_zeros+zeros

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
        print("~")
# } Driver Code Ends
