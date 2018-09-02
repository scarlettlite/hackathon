from collections import Counter
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t: return ""
        ct = Counter(t)
        beg, end = 0, 0
        mi, mj = 0, float('inf')
        for i, c in enumerate(s):
            if c in ct:
                ct[c] -= 1
                end = i 
            if all(value <= 0 for key, value in ct.items()) and c in ct:
                while beg < end and (s[beg] not in ct or ct[s[beg]] < 0):
                    if s[beg] in ct:
                        ct[s[beg]] += 1
                    beg += 1
                if mj - mi > end - beg:
                    mi, mj = beg, end
        ans = s[mi:mj+1]
        return ans

print(Solution().minWindow("", "ABC"))

        