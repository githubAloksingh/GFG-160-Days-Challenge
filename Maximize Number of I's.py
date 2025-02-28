class Solution:
    # k is the maximum number of zeros allowed to flip
    def maxOnes(self, arr, k):
        # code here
        left=0
        max_length=0
        flip_count=0
        
        for right in range(len(arr)):
            if arr[right]==0:
                flip_count+=1
                
            while flip_count>k:
                if arr[left]==0:
                    flip_count-=1
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())  # Number of test cases
    for _ in range(t):
        arr = list(map(int,
                       input().strip().split()))  # Read the array of 0s and 1s
        m = int(input().strip())  # Maximum number of zeros allowed to flip
        ans = Solution().maxOnes(arr, m)
        print(ans)

# } Driver Code Ends
