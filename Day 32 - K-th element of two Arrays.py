#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        arr3=[]
        i,j=0,0
        m=len(a)
        n=len(b)
        while i<m and j<n:
            if a[i]<b[j]:
                arr3.append(a[i])
                i+=1
            else:
                arr3.append(b[j])
                j+=1
        while i<m:
            arr3.append(a[i])
            i+=1
        while j<n:
            arr3.append(b[j])
            j+=1
                
        return arr3[k-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
