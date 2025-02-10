class Solution:
    def search(self,index, i,j, mat,word):
        m=len(mat)
        n=len(mat[0])
        if index==len(word):
            return True
        if i<0 or j<0 or i>=m or j>=n or mat[i][j]!=word[index]:
            return False
            
        temp=mat[i][j]
        mat[i][j]='$'
        
        ans=(self.search(index+1,i+1,j,mat,word)or
            self.search(index+1,i-1,j,mat,word)or
            self.search(index+1,i,j+1,mat,word)or
            self.search(index+1,i,j-1,mat,word))
            
            
        mat[i][j]=temp
        return ans
    
	def isWordExist(self, mat, word):
		#Code here
		m=len(mat)
		n=len(mat[0])
		
		for i in range(m):
		    for j in range(n):
		        if mat[i][j]==word[0]:
		            if self.search(0, i,j,mat, word):
		                return True
		return False
		               


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
