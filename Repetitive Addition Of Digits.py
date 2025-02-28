class Solution:
    def singleDigit(self, n):
    	#code here 
    	num=n
    	while num>=10:
    	    sum_digits=0
    	    while num>0:
    	        sum_digits+=num%10
    	        num//=10
    	    num=sum_digits
    	    
        return num

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.singleDigit(N)
        print(ans)
        print("~")

# } Driver Code Ends
