#User function Template for python3
class Solution:
    def twoSum(self, arr, target):
        # code here
        arr.sort()
        left=0
        right=len(arr)-1
        while left<right:
            sum=arr[left]+arr[right]
            if sum==target:
                return True
            elif sum<target:
                left+=1
            else:
                right-=1
        return False
        
