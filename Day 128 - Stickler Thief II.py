class Solution:
    def solve(self, arr,i,n,memo):
        if i>n:
            return 0
        if i in memo:
            return memo[i]
        steal=arr[i]+self.solve(arr,i+2,n,memo)
        skip=self.solve(arr,i+1,n,memo)
        memo[i]=max(steal,skip)
        return memo[i]
    def maxValue(self, arr):
        # code here
        n=len(arr)
        i=0
        memo1={}
        if n==1:
            return arr[0]
        if n==2:
            return max(arr[0], arr[1])
        memo2={}
        take_0th_index=self.solve(arr,0,n-2,memo1)
        take_1_th_index=self.solve(arr, 1,n-1, memo2)
        return max(take_0th_index,take_1_th_index)


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends
