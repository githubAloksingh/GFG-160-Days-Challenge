import heapq
class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        jobs=list(zip(deadline,profit))
        jobs.sort()
        min_heap=[]
        for d,p in jobs:
            if len(min_heap)<d:
                heapq.heappush(min_heap,p)
            elif min_heap and p>min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,p)
        return [len(min_heap), sum(min_heap)]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        deadline = list(map(int, input().strip().split()))
        profit = list(map(int, input().strip().split()))

        obj = Solution()
        ans = obj.jobSequencing(deadline, profit)
        print(ans[0], ans[1])
        print("~")
# } Driver Code Ends
