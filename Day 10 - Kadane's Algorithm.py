class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        n=len(arr)
        sum=0
        maxi=float('-inf')
        for i in range(n):
            sum+=arr[i]
            
            if sum>maxi:
                maxi=sum
            if sum<0:
                sum=0
        return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
