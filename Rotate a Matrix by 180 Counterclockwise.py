#User function Template for python3

class Solution:
	def rotateMatrix(self, mat):
		# Code here
		res=[]
		n=len(mat)
		for _ in range(n):
		    res.append([0]*n)
		
		for i in range(n):
		    for j in range(n):
		        res[i][j]=mat[n-i-1][n-1-j]
	    for i in range(n):
	        for j in range(n):
	            mat[i][j]=res[i][j]
		        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ob.rotateMatrix(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends
