#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3
class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        if e==0:
            return 1.0
        if e<0:
            return 1/self.power(b,-e)
        if e%2==0:
            return self.power(b*b,e//2)
        else:
            return b*self.power(b*b,(e-1)//2)

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        b = float(input())
        e = int(input())
        ob = Solution()
        result = ob.power(b, e)
        print(f"{result:.5f}")
        print("~")
# } Driver Code Ends
