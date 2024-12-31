 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        if not arr:
            return 0
        arr.sort()
        max_length=1
        curr_length=1
        for i in range(1, len(arr)):
            if arr[i]==arr[i-1]:
                continue
            elif arr[i]==arr[i-1]+1:
                curr_length+=1
            else:
                max_length=max(max_length, curr_length)
                curr_length=1
        max_length=max(max_length, curr_length)
        return max_length
        





