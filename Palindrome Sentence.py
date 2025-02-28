#User function Template for python3
class Solution:
	def sentencePalindrome(self, s):
		# your code here
		result=""
		for ch in s:
		    if ch.isalnum():
		        result+=ch.lower()
		return result==result[::-1]
		        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        s = input()
        ob = Solution()
        if ob.sentencePalindrome(s):
            print("true")
        else:
            print("false")

# } Driver Code Ends
