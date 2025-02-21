
class Solution:
    def isBalanced(self, s):
        # code here
        stack=[]
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if (ch==')'and stack[-1]=='(') or \
                   (ch=='}' and stack[-1]=='{') or \
                   (ch ==']' and stack[-1]=='['):
                   stack.pop()
                else: 
                    return False
        return not stack
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        obj = Solution()
        if obj.isBalanced(s):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
