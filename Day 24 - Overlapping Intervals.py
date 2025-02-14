class Solution:
	def mergeOverlap(self, arr):
		#Code here
		arr.sort(key=lambda x:x[0])
		ans=[]
		for interval in arr:
		    start,end=interval
		    if ans and ans[-1][1]>=start:
		        ans[-1][1]=max(ans[-1][1],end)
		    else:
		        ans.append([start, end])
		        
		return ans


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends
