class Solution:

    def removeDuplicates(self, s):
        x = s[0]
        for i in range(1, len(s)):
            if s[i] not in x:
                x += s[i]
        return x




pal = Solution()
print(pal.removeDuplicates("abbacbd"))