
class Solution:
    def maxLength(self, s):
        # code here
        stack=[-1]
        maxi=0
        for i, char in enumerate(s):
            if char=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                    
                else:
                    maxi=max(maxi, i-stack[-1])
        return maxi
                


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends
