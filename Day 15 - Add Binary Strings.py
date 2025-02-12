#User function Template for python3
class Solution:
    def addBinary(self, s1, s2):
		# code here
		i, j=len(s1)-1, len(s2)-1
		carry=0
		result=[]
		while i>=0 or j>=0 or carry:
		    bit1=int(s1[i])if i>=0 else 0
		    bit2=int(s2[j]) if j>=0 else 0
		    total=bit1+bit2+carry
		    carry=total//2
		    result.append(str(total%2))
		    i-=1
		    j-=1
        while len(result)>1 and result[-1]=='0':
            result.pop()
	    return ''.join(result[::-1])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends
