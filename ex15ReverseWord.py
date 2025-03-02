class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, s):
        l = s.split() # split the string in a list
        l.reverse()
        return ' '.join(l)


rev = Solution()
print(rev.reverseWords(" i like   this program   very   much "))