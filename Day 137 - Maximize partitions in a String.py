class Solution:
    def maxPartitions(self , s):
        # code here
        last_occurence={}
        n=len(s)
        for i in range(n):
            last_occurence[s[i]]=i
        partitions=0
        end=0
        for i in range(n):
            end=max(end,last_occurence[s[i]])
            if i==end:
                partitions+=1
        return partitions

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends
