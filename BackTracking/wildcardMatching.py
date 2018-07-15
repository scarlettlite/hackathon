class Solution:
    def backtrack(self,p,s):
        if p == "*" : return True
        if not p and not s: return True
        if not p or not s: return False
        if p[0] == s[0] or p[0] == "?":
            if self.backtrack(p[1:],s[1:]): return True
        if p[0] == '*':
            if self.backtrack(p[1:],s): return True
            if self.backtrack(p,s[1:]): return True
        return False
        

        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        """
        Add 1 for empty string
        """
        x = ""
        a = 0
        while a < len(p):
            if a > 0 and p[a-1] == "*" and p[a] == "*":
                a+=1
                continue
            x += p[a]
            a+=1
        p = x

        return self.backtrack(p,s)

print(Solution().isMatch("aghc", "?*?*"))