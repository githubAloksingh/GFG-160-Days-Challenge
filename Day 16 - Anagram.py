#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        charCount={}
        for ch in s1:
            charCount[ch]=charCount.get(ch,0)+1
        for ch in s2:
            charCount[ch]=charCount.get(ch,0)-1
        for key, value in charCount.items():
            if value!=0:
                return False
        return True
            
