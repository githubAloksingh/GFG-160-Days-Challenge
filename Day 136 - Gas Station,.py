class Solution:
    def startStation(self, gas, cost):
        # Your code here
        if sum(gas)<sum(cost):
            return -1
        n=len(gas)
        total=0
        result=0
        for i in range(n):
            total+=gas[i]-cost[i]
            if total<0:
                total=0
                result=i+1
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        gas = list(map(int, input().strip().split()))
        cost = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.startStation(gas, cost)
        print(ans)
        print("~")

# } Driver Code Ends
