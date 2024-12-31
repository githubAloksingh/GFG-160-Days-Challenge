# Brute Force Approach
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
        for i in range(0, len(arr)-1):
            if arr[i]==arr[i+1]:
                continue
            elif arr[i]+1==arr[i+1]:
                curr_length+=1
            else:
                curr_length=1
            max_length=max(max_length, curr_length)
        return max_length
        


# Optimal Approach
 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        nums=set(arr)
        maxi=0
        for num in nums:
            if num-1 not in nums:
                curr_num=num
                curr_len=1
                while curr_num+1 in nums:
                    curr_num+=1
                    curr_len+=1
                maxi=max(curr_len,maxi)
        return maxi












        





