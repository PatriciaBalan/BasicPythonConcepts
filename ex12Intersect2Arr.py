#Given two sorted arrays arr1[] and arr2[].
# Your task is to return the intersection of both arrays.

#Intersection of two arrays is said to be elements that are common in both arrays.
# The intersection should not count duplicate elements.

#Note: If there is no intersection then return an empty array.

class Solution:
    #Function to return a list containing the intersection of two arrays.
    def intersection(self, arr1, arr2):

        s1 = len(arr1)
        s2 = len(arr2)
        comm = []

        for i in range(s1):
            for j in range(s2):
                if arr1[i] == arr2[j]:
                    comm.append(arr1[i])
            i += 1
        return comm


s=Solution()
print(s.intersection([1, 2, 3, 4], [2, 4, 6, 7, 8]))




#c = list((set(arr1) & set(arr2)))
   #     return sorted(c)