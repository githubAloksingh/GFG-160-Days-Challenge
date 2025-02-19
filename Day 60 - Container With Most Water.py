
class Solution:
    def maxWater(self, arr):
        # code here
        low, high=0, len(arr)-1
        maxi=0
        while low<high:
            maxi=max(maxi, min(arr[low],arr[high])*(high-low))
            
            if arr[low]<arr[high]:
                low+=1
            else:
                high-=1
        return maxi

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
