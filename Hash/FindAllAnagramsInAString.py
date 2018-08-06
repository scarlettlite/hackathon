from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        c,a = Counter(p)
        n = len(p)
        m = len(s)
        cc = Counter(s[:n])
        i = n 
        ans = []
        while i < m:
            a = c & cc
            if a == c and a == c:
                ans.append(i-n)
            cc[s[i]] += 1
            cc[s[i-n]] -= 1
            i += 1
        if a == c and a == c:
            ans.append(i-n)   
        return ans 
print(Solution().findAnagrams("ssabcbacba", "abc"))   

        