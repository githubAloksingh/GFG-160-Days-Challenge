#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends


class Solution:
    def getMaxArea(self,arr):
        #code here
        stack=[]
        max_area=0
        n=len(arr)
        for i in range(n+1):
            while stack and (i==n or arr[i]<arr[stack[-1]]):
                height=arr[stack.pop()]
                if not stack:
                    width=i
                else:
                    width=i-stack[-1]-1
                max_area=max(max_area, height*width)
            stack.append(i)
        return max_area


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getMaxArea(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends
