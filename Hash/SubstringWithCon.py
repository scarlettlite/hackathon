"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
"""
from collections import Counter
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s: return []
        i, n, l = 0, len(s), len(words[0])
        sw = Counter(words)
        ans = []
        if any(l != len(word) for word in words):
            return []
        while i < n:
            while i<n and s[i:i+l] not in sw:
                i += 1
            ts = list()
            while i<n and s[i:i+l] in sw and len(ts) < len(words):
                ts.append(s[i:i+l])
                i += l
            if Counter(ts) & sw == sw:
                ans.append(i - len(ts)*l)
                i = i - ((len(words)-1) * l )
            else:
                i = i - (len(ts)*l) + 1
        return ans

#print(Solution().findSubstring("barfoethebarfoeman", ["foe","bar","the"]))
print(Solution().findSubstring("wordgoodwordgoodbestword",
["word","good","best","word"]))          
