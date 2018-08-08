class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        i, j = 0, 0
        while i < m and j < n:
            while j < n and s[i] != t[j]:
                j += 1
            if j == n and i < m:
                break
            else:
                i += 1
                j += 1
       
        if j == n and i < m:
            return False
        return True

print(Solution().isSubsequence("acb", "ahbgdc"))