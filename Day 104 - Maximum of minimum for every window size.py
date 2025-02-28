
class Solution:
    def maxOfMins(self, arr):
       # code here
       n=len(arr)
       left=[-1]*n
       right=[n]*n
       stack=[]
       for i in range(n):
           while stack and arr[stack[-1]]>=arr[i]:
               stack.pop()
           if stack:
               left[i]=stack[-1]
           stack.append(i)
       stack.clear()
       
       for i in range(n-1,-1,-1):
           while stack and arr[stack[-1]]>=arr[i]:
               stack.pop()
           if stack:
               right[i]=stack[-1]
           stack.append(i)
       res=[0]*(n+1)
       for i in range(n):
           window_size=right[i]-left[i]-1
           res[window_size]=max(res[window_size], arr[i])
           
       for i in range(n-1, 0,-1):
           res[i]=max(res[i],res[i+1])
       return res[1:]
    

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        solution = Solution()
        result = solution.maxOfMins(arr)
        print(" ".join(map(str, result)))
        print("~")
# } Driver Code Ends
