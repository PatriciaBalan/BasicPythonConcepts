#Given two arrays a[] and b[], the task is to find the number of elements in the
# union between these two arrays.
from operator import countOf


#The Union of the two arrays can be defined as the set containing distinct elements from both arrays.
# If there are repetitions, then only one element occurrence should be there in the union.

#Note: Elements of a[] and b[] are not necessarily distinct.

class Solution:
    #Function to return the count of number of elements in union of two arrays.

    def findUnion(self, a, b):

        union_list = list(set(a).union(b)) #union of two list
        #union = a.update(b)
        #print(union)
        print(union_list)
        print(len(union_list)) # no of values of a list

s=Solution()
s.findUnion([85, 25, 1, 32, 54, 6], [85, 2])



