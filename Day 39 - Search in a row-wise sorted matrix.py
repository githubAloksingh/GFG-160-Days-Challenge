
#User function Template for python3

class Solution:
    
    def search(self, mat, x):
        low, high=0, len(mat)-1
        while low<=high:
            mid=low+(high-low)//2
            if mat[mid]==x:
                return True
            elif mat[mid]>x:
                high=mid-1
            else:
                low=mid+1
        return False
    
    
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
    	# code here 
    	n,m=len(mat),len(mat[0])
    	for i in range(n):
    	    if self.search(mat[i], x):
    	        return True
    	return False
    	



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchRowMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends
