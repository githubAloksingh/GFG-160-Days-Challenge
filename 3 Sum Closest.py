#User function Template for python3

class Solution:
    def closest3Sum(self, arr, target):
        # code here
        n=len(arr)
        arr.sort()
        closest_sum=arr[0]+arr[1]+arr[2]
        for i in range(n-2):
            
            left, right = i+1, n-1
            while left<right:
                curr_sum=arr[i]+arr[left]+arr[right]
                if abs(curr_sum-target) < abs(closest_sum-target):
                    closest_sum=curr_sum
                elif abs(curr_sum-target) == abs(closest_sum-target):
                    closest_sum=max(closest_sum,curr_sum)
                if curr_sum<target:
                    left+=1
                else:
                    right-=1
        return closest_sum
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        print(ob.closest3Sum(arr, target))
        print("~")

# } Driver Code Ends
