
class Solution:
    def maxWater(self, arr):
        # code here
        if not arr:
            return 0
        left,right=0,len(arr)-1
        left_max,right_max=arr[left],arr[right]
        total=0
        while left<right:
            if arr[left]<arr[right]:
                if arr[left]<left_max:
                    total+=left_max-arr[left]
                else:
                    left_max=arr[left]
                left+=1
                
            else:
                if arr[right]<right_max:
                    total+=right_max-arr[right]
                else:
                    right_max=arr[right]
                right-=1
        return total
                

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
