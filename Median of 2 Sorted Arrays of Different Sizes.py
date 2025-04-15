#User function Template for python3

class Solution:
    def medianOf2(self, a, b):
        #code here
        i=j=0
        merged=[]
        
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                merged.append(a[i])
                i+=1
            else:
                merged.append(b[j])
                j+=1
                
        while i<len(a):
            merged.append(a[i])
            i+=1
        while j<len(b):
            merged.append(b[j])
            j+=1
        n=len(merged)
        mid=n//2
        if n%2==0:
            return (merged[mid-1]+merged[mid])/2
        else:
            return merged[mid]
            

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]

        ob = Solution()

        if len(arr2) == 1 and arr2[0] == 0:
            arr2 = []
        ans = ob.medianOf2(arr1, arr2)
        if int(ans) == ans:
            print(int(ans))
        else:
            print(ans)
        print("~")

# } Driver Code Ends
