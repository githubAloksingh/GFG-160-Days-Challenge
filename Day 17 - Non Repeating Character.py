#User function Template for python3

class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        # n=len(s)
        # for i in range(n):
        #     found=False
        #     for j in range(n):
        #         if i!=j and s[i]==s[j]:
        #             found =True
        #             break
        #     if not found:
        #         return s[i]
        # return '$'
        map={}
        for ch in s:
            map[ch]=map.get(ch,0)+1
        for ch in s:
            if map[ch]==1:
                return ch
        return '$'
    
