#Given an array arr. Your task is to find the minimum and maximum elements in the array.
#Note: Return a Pair that contains two elements the first one will be a minimum element
#   and the second will be a maximum.

class Solution:
    def get_min_max(self, arr):
        self.arr = arr
        min = arr[0]
        max = arr[0]
        size = len(arr)
        for i in range(len(arr)):
            if (arr[i] > max):
                max = arr[i]
        for i in range(len(arr)):
            if (arr[i] < min):
                min = arr[i]
        return (min, max)

sol = Solution()
print(sol.get_min_max([3, 2, 1, 56, 10000, 167]))







