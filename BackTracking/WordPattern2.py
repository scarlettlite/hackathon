from collections import defaultdict
class Solution:
    def __init__(self):
        self.pp = defaultdict(str)
        self.ss = defaultdict(str)
        self.cache = {}

    def helper(self, pattern, string):
        if string == "" and pattern == "":
            return True
        elif string == "" or pattern == "":
            return False
        else:
            for k in range(1, len(string)+1):
                p, s = pattern[0], string[:k]
                if self.pp.get(p, None) == None and self.ss.get(s, None) == None:
                    self.pp[p] = s
                    self.ss[s] = p
                    result = self.helper(pattern[1:], string[k:])
                    if result == True:
                        return True
                    del self.pp[p]
                    del self.ss[s]
                elif self.pp.get(p, None) != s or self.ss.get(s, None) != p:
                    continue
                elif self.pp.get(p, None) == s and self.ss.get(s, None) == p:
                    result = self.helper(pattern[1:], string[k:])
                    if result == True:
                        return True
            return False
                    
    def wordPatternMatch(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.helper(pattern, string)

print(Solution().wordPatternMatch("aba", "aaaa"))
        
