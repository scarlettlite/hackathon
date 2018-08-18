"""
https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/
"""

class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        n = len(p)
        issub = [[False if i != j else True for _ in range(n)] False for _ in range(n)]
        for j in range(1, n):
            for l in range(2, j+1):
                i = j - l + 1
                
                ord(s[j]) == ord(s[j-1]) + 1 and issub[i][j-1] == True:
