from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False
        match = Counter(s1)
        j , m = 0, len(s2)
        to = Counter()
        n  = len(s1)
        while j < n:
            to[s2[j]] += 1
            j += 1
        while j <= m:
            if match == to:
                return True
            if j < m:
                k = j - n
                to[s2[k]] -= 1
                if to[s2[k]] == 0:
                    del to[s2[k]]
                to[s2[j]] += 1
            j += 1
        return False


print(Solution().checkInclusion("ab", "eidbaooo"))

