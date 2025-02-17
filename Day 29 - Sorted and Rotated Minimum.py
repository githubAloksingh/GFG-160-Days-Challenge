#User function Template for python3

class Solution:
    def findMin(self, arr):
        #complete the function here
        low, high=0, len(arr)-1
        while low<high:
            mid=low+(high-low)//2
            if arr[mid]>arr[high]:
                low=mid+1
            else:
                high=mid
        return arr[low]


#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
