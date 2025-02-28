#User function Template for python3
class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        total_sum=sum(arr)
        if total_sum%3!=0:
            return [-1, -1]
            
        prefix_sum, i, j=0,-1,-1
        target=total_sum//3
        for index in range(len(arr)):
            prefix_sum+=arr[index]
            if prefix_sum==target and i==-1:
                i=index
            elif prefix_sum==2*target and j==-1 and i!=-1:
                j=index
                return [i, j]
        return [-1, -1]
#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if (result == [-1, -1]) or len(result) != 2:
            print("false")

        else:
            sum1 = sum2 = sum3 = 0
            for i in range(len(arr)):
                if i <= result[0]:
                    sum1 += arr[i]
                elif i <= result[1]:
                    sum2 += arr[i]
                else:
                    sum3 += arr[i]

            if sum1 == sum2 == sum3:
                print("true")
            else:
                print("false")
        print("~")
# } Driver Code Ends
