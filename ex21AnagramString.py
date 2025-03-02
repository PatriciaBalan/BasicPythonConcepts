class Solution:

    # Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        news1= ''.join(sorted(s1))
        news2= ''.join(sorted(s2))
        if(news1 in news2 and len(news1) == len(news2)):
            for i in range(len(news1)):
                for j in range(len(news2)):
                    if news1[i] == news2[j]:
                        pass
                i +=1
                return True
        else:
            return False


pal = Solution()
print(pal.areAnagrams("geeks", "kseea"))

