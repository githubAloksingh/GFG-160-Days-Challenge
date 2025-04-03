# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        n=len(arr)
        max_length=0
        prefix_sum=0
        sum_map={}
        for i in range(n):
            prefix_sum+=arr[i]
            
            if prefix_sum==k:
                max_length=i+1
            if prefix_sum-k in sum_map:
                max_length=max(max_length,i-sum_map[prefix_sum-k])
            if prefix_sum not in sum_map:
                sum_map[prefix_sum]=i
        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends
