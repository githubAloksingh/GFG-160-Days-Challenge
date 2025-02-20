import heapq
class Solution:
    def getMedian(self, arr):
        left=[]
        right=[]
        medians=[]
        for num in arr:
            if not left or num <= -left[0]:
                heapq.heappush(left,-num)
            else:
                heapq.heappush(right, num)
            
            if len(left)>len(right)+1:
                heapq.heappush(right, -heapq.heappop(left))
                
            elif len(right)>len(left):
                    heapq.heappush(left, -heapq.heappop(right))
            
            if len(left)>len(right):
                medians.append(float(-left[0]))
            else:
                medians.append(((-left[0]+right[0])/2.0))
        return medians
#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends
