#User function template for Python
import sys
class Solution:
    def myAtoi(self, s):
        # Code here
        INT_MAX=2**31-1
        INT_MIN=-2**31
        
        s=s.lstrip()
        
        sign=1
        if len(s)>0 and s[0]=='-':
            sign=-1
            s=s[1:]
        elif len(s)>0 and s[0]=='+':
            s=s[1:]
        result=0
        for char in s:
            if char.isdigit():
                result=result*10+int(char)
            else:
                break
        result=result*sign
        
        if result>INT_MAX:
            return INT_MAX
        if result<INT_MIN:
            return INT_MIN
        return result
            
            

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends
