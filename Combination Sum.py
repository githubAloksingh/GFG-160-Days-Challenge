#User function Template for python3

class Solution:
    
    # Function to find all combinations of elements
    # in array arr that sum to target.
    def __init__(self):
        self.result=[]
    def find_combination(self, index, arr,target,curr):
        if target==0:
            self.result.append(list(curr))
            return 
        if index>=len(arr) or target<0:
            return 
        curr.append(arr[index])
        self.find_combination(index, arr,target-arr[index], curr)
        curr.pop()
        
        self.find_combination(index+1, arr, target, curr)
    def combinationSum(self, arr, target):
        # code here
        self.result=[]
        curr=[]
        self.find_combination(0, arr, target,curr)
        return self.result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))
        sum = int(input())
        ob = Solution()
        ans = ob.combinationSum(arr, sum)
        if (len(ans) == 0):
            print(-1)
        else:
            for i in range(len(ans)):
                ans[i].sort()
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()
        print("~")

# } Driver Code Ends
