#User function Template for python3
from functools import cmp_to_key
class Solution:
    @staticmethod
    def compare(x,y):
        if x+y>y+x:
            return -1
        elif x+y<y+x:
            return 1
        else:
            return 0
    

	def findLargest(self,arr):
	    # code here
	    str_arr=[]
	    for num in arr:
	        str_arr.append(str(num))
	    str_arr.sort(key=cmp_to_key(Solution.compare))
	    if str_arr[0]=="0":
	        return "0"
	    return ''.join(str_arr)
	    
	    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends
