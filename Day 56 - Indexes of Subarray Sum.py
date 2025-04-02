#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        cnt=0
        n=len(arr)
        for i in range(n):
            curr_sum=0
            for j in range(i,n):
                curr_sum+=arr[j]
                if curr_sum==target:
                    return [i+1,j+1]
                elif curr_sum>target:
                    break
        return [-1]
                

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends
