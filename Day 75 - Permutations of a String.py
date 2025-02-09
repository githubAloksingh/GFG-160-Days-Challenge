#User function Template for python3

class Solution:
    def solve(self, s, index, result):
        if index==len(s):
            result.append("".join(s))
            return
        
        unique_set=set()
        for i in range(index, len(s)):
            
            if s[i] in unique_set:
                continue
            unique_set.add(s[i])

            s[index],s[i]=s[i], s[index]
            self.solve(s, index+1, result)
            s[index],s[i]=s[i], s[index]
    
    
    
    def findPermutation(self, s):
        # Code here
        result=[]
        s=list(s)
        self.solve(s,0,result)
        return result
       
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends
