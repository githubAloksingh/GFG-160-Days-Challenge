import heapq
class Solution:
    def longestSubarray(self, arr, x):
        #code here 
        max_heap=[]
        min_heap=[]
        n=len(arr)
        i=0
        max_len=0
        for j in range(n):
            heapq.heappush(max_heap,(-arr[j],j))
            heapq.heappush(min_heap,(arr[j],j))
            while -max_heap[0][0]-min_heap[0][0]>x:
                i=min(max_heap[0][1],min_heap[0][1])+1
                while max_heap[0][1]<i:
                    heapq.heappop(max_heap)
                while min_heap[0][1]<i:
                    heapq.heappop(min_heap)
            if j-i+1>max_len:
                max_len=j-i+1
                start_idx=i
        return arr[start_idx:start_idx+max_len]
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.longestSubarray(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends
