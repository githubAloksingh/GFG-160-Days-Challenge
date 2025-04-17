#User function Template for python3

class Solution:
    def numOfSubset(self, arr):
        # Your code goes here
        cnt=1
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i]+1!=arr[i+1]:
                cnt+=1
        return cnt
#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        ob = Solution()
        print(ob.numOfSubset(nums))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
