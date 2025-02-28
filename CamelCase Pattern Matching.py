#User function Template for python3

class Solution:
    def camelCase(self,arr,pat):
        #code here
        result=[]
        for word in arr:
            upper_case=""
            for ch in word:
                if ch.isupper():
                    upper_case+=ch
            if upper_case.startswith(pat):
                result.append(word)
        return sorted(result)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(str, input().split()))
        pat = input()
        ob = Solution()
        ans = ob.camelCase(arr, pat)
        ans.sort()
        if not ans:  # Check if ans is empty
            print("[]")
        else:
            for i in ans:
                print(i, end=" ")
            print()

# } Driver Code Ends
