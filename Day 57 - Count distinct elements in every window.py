class Solution:
    def count_unique(self, arr):
        return len(set(arr))
    def countDistinct(self, arr, k):
        # Code here
        res=[]
        n=len(arr)
        if k>n:
            return []
        for i in range(n-k+1):
            cnt=self.count_unique(arr[i:i+k])
            res.append(cnt)
        return res

#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends
