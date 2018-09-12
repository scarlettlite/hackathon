"""https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/"""
class Solution:
    def issubsequence(self, s, t):
        if not s and t: return False
        if s and not t: return True
        if not s and not t : return True
        i, j = 0, 0
        m, n = len(s), len(t)
        while i < m and j < n:
            while i < m and s[i] != t[j]:
                i += 1
            j += 1
            i += 1
        if i <= m and j == n:
            return True
        return False

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        ans = ""
        for word in d:
            if self.issubsequence(s, word):
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans):
                    ans = min(word, ans)
        return ans

print(Solution().findLongestWord("abpcplea", ["ale","apple","monkey","plea"]))
            
