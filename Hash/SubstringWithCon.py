from collections import Counter, defaultdict
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s: return []
        n, l = len(s), len(words[0])
        sw = Counter(words)
        ans = []
        if any(l != len(word) for word in words):
            return []
        i = 0
        idxdict = {}
        while i <= n - l:
            x = s[i:i+l]
            if x in sw:
                idxdict[i] = x
            i += 1
        listsize = len(words) * l
        for key in idxdict.keys():
            if len(s) - key < listsize:
                break
            ts = [idxdict[key]]
            i = key + l
            while i in idxdict and len(ts) < len(words):
                ts.append(idxdict[i])
                i += l
            if Counter(ts) & sw == sw:
                ans.append(key)
        return ans

print(Solution().findSubstring("barfoofoobarthefoobarman",
["bar","foo","the"]))
# print(Solution().findSubstring("wordgoodwordgoodbestword",
# ["word","good","best","word"]))          
