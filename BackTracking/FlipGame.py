class Solution:
    def helper(self, s):
        for i in range(1, len(s)):
            if s[i] == '+' and s[i-1] == '+':
                s[i], s[i-1] = '-', '-'
                if not self.helper(s):
                    s[i], s[i-1] = '+', '+'
                    return True
                s[i], s[i-1] = '+', '+'
        return False

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = self.helper(list(s))
        return ans