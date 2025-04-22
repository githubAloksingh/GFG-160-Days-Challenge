class Solution:
    def longestValidWord(self, words):
        # code here
        words.sort()
        longest=""
        st=set()
        for word in words:
            if len(word)==1 or word[:-1] in st:
                st.add(word)
                if len(word)>len(longest):
                    longest=word
        return longest

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        line = input().strip()
        arr = line.split()
        sol = Solution()
        ans = sol.longestValidWord(arr)
        print(ans)
        print("~")
# } Driver Code Ends
