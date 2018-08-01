from collections import defaultdict
class Solution:
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern = list(pattern)
        string = string.split(' ')
        if len(pattern) != len(string):
            return False
        dd = defaultdict(str)
        ee = defaultdict(str)
        for a,b in zip(string, pattern):
            if dd.get(a, None) == None and ee.get(b, None) == None:
                dd[a] = b
                ee[b] = a
            elif dd[a] != b or ee[b] != a:
                return False
        return True

print(Solution().wordPattern("abba",
"dog cat cat fish"))
