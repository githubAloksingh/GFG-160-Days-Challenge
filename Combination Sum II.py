#User function Template for python3

class Solution: 
    def __init__(self): 
        self.result=[]
    def backtrack(self, index, arr, target,curr): 
        if target==0:
            self.result.append(curr[:]) 
            return 
        for i in range(index, len(arr)):
            if i>index and arr[i]==arr[i-1]:
                continue
            if(arr[i]>target):
                break
            curr.append(arr[i])
            self.backtrack(i+1,arr,target-arr[i],curr)
            curr.pop()
        
    # Function to find all combinations of elements
    # in array arr that sum to target.
    def uniqueCombinations(self, arr, target):
        # code here
        self.result=[]
        curr=[]
        arr.sort()
        self.backtrack(0,arr,target,curr)
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
        ans = ob.uniqueCombinations(arr, sum)
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
