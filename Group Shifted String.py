class Solution:
    def shift_pattern(self,s):
        if len(s)==1:
            return ""
        pattern=[]
        for i in range(1,len(s)):
            diff=(ord(s[i])-ord(s[i-1]))%26
            pattern.append(str(diff))
        return ','.join(pattern)
    def groupShiftedString(self, arr):
        #code here
        groups=defaultdict(list)
        for string in arr:
            pattern=self.shift_pattern(string)
            groups[pattern].append(string)
            
        return list(groups.values())
#{ 
 # Driver Code Starts
from collections import defaultdict

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = input().split()
        sol = Solution()
        result = sol.groupShiftedString(arr)
        for group in result:
            group.sort()
        result.sort(key=lambda x: x[0])
        for group in result:
            print(" ".join(group))
        print("~")

# } Driver Code Ends
