#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        union =set()
        for num in a:
            union.add(num)
        for num in b:
            union.add(num)
        return len(union)
