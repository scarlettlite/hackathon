class Solution(object):
    def rev(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s.isspace(): return s
        n = len(s)
        s = list(s)
        i, j = 0, 0
        while i < n:
            while j < n and s[j] != ' ':
                j += 1
            self.rev(s, i, j-1)
            i = j + 1
            j += 1
        self.rev(s, 0, n-1)
        s = ''.join(s)
        return s

print(Solution().reverseWords(' '))