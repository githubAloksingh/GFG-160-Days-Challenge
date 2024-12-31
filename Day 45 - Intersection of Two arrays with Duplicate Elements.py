
class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        set_a=set(a)
        set_b=set(b)
        intersection =[]
        for i in set_a:
            if i in set_b:
                intersection.append(i)
        return intersection
