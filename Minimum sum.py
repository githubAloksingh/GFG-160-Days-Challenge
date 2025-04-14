#User function Template for python3

class Solution:
    def add_large_numbers(self, num1,num2):
        result=[]
        carry=0
        max_len=max(len(num1),len(num2))
        num1=num1.zfill(max_len)
        num2=num2.zfill(max_len)
        
        for i in range(max_len-1,-1,-1):
            digit_sum=int(num1[i]) + int(num2[i]) +carry
            result.append(str(digit_sum%10))
            carry=digit_sum//10
        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])
        
    def minSum(self, arr):
        # code here
        arr.sort()
        if len(arr)==1:
            return arr[0]
        num1=""
        num2=""
        for i in range(len(arr)):
            if i%2==0:
                num1+=str(arr[i])
            else:
                num2+=str(arr[i])
        result=self.add_large_numbers(num1, num2)
        result=result.lstrip('0')
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends
