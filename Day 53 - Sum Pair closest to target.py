#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        arr.sort()
        n=len(arr)
        res=[]
        left,right=0,n-1
        closest_sum=float('inf')
        while left<right:
            curr_sum=arr[left]+arr[right]
            if abs(curr_sum-target) <abs(target-closest_sum):
                closest_sum=curr_sum
                res=[arr[left], arr[right]]
            elif curr_sum<target:
                left+=1
            elif curr_sum>target:
                right-=1
            else:
                return res
        return res
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        arr.sort()
        n=len(arr)
        res=[]
        left,right=0,n-1
        closest_sum=float('inf')
        while left<right:
            curr_sum=arr[left]+arr[right]
            if abs(curr_sum-target) <abs(target-closest_sum):
                closest_sum=curr_sum
                res=[arr[left], arr[right]]
            elif curr_sum<target:
                left+=1
            elif curr_sum>target:
                right-=1
            else:
                return res
        return res
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
