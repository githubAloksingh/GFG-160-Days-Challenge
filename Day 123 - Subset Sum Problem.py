class Solution:
    def check(self, arr,i, target):
        if target==0:
            return True
        if i>=len(arr):
            return False
        if arr[i]>target:
            return self.check(arr,i+1, target)
        return self.check(arr, i+1, target-arr[i]) or self.check(arr, i+1, target)
        
    def isSubsetSum (self, arr, sum):
        # code here 
        
        return self.check(arr, 0,sum)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends
