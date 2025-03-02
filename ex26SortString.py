class Solution:
    def sort(self, s):
        #return sorted(s)
        return "".join(sorted(s))

s = "fgdndc"
p = Solution()
print(p.sort(s))