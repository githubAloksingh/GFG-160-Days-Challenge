#User function Template for python3
class Solution:
    def spiralFill(self, n, m, arr):
        # code here
        res=[]
        for _ in range(n):
            res.append([0]*m)
        top,bottom,left,right=0,n-1,0,m-1
        idx=0
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                res[top][i]=arr[idx]
                idx+=1
            top+=1
            for i in range(top,bottom+1):
                res[i][right]=arr[idx]
                idx+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    res[bottom][i]=arr[idx]
                    idx+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res[i][left]=arr[idx]
                    idx+=1
                left+=1
        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3
class Array:

    @staticmethod
    def input(A, n):
        A[:] = list(map(int, input().split()))

    @staticmethod
    def print(A):
        print(" ".join(map(str, A)))


class Matrix:

    @staticmethod
    def input(A, n, m):
        for i in range(n):
            A.append(list(map(int, input().split())))

    @staticmethod
    def print(A):
        for row in A:
            print(" ".join(map(str, row)))


# Main function
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        m = int(input())
        arr = [0] * (n * m)
        Array.input(arr, n * m)

        obj = Solution()
        res = obj.spiralFill(n, m, arr)

        Matrix.print(res)
        print("~")

# } Driver Code Ends
