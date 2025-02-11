#Your Function should return a list containing all possible IP address
from typing import List
class Solution:
    def __init__(self):
        self.result=[]
        self.n=0
    def isValid(self,s:str)->bool:
        if s[0]=='0' and len(s)>1:
            return False
        val=int(s)
        return val<=255
        
    def solve(self,s,idx,part,curr):
        if idx==self.n and part==4:
            self.result.append(curr[:-1])
            return 
        if idx+1<=self.n:
            self.solve(s,idx+1,part+1,curr+s[idx:idx+1]+".")
            
        if idx+2<=self.n and self.isValid(s[idx:idx+2]):
            self.solve(s,idx+2,part+1,curr+s[idx:idx+2]+".")
            
        if idx+3<=self.n and self.isValid(s[idx:idx+3]):
            self.solve(s,idx+3,part+1,curr+s[idx:idx+3]+".")
        

    
    
    
    
    def generateIp(self, s):
        # Code here
        self.result=[]
        self.n=len(s)
        if len(s)>12:
            return self.result
            
        self.solve(s,0,0,"")
        return self.result


#{ 
 # Driver Code Starts
#Main
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        res = Solution().generateIp(s)
        res.sort()
        if (len(res)):
            for u in res:
                print(u)
        else:
            print(-1)
        print("~")

# } Driver Code Ends
