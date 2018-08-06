class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        ss = dict()
        tt = dict()
        for a,b in zip(s,t):
            if a not in ss and b not in tt:
                ss[a] = b
                tt[b] = a
            elif ss.get(a, None) == b and tt.get(b, None) == a:
                continue
            else:
                return False
        return True

print(Solution().isIsomorphic("xsw", "awe"))