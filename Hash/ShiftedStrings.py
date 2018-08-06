import collections
class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        def computeKey(s):
            key = []
            first = None
            for i,c in enumerate(s):
                if i == 0:
                    first = c
                digit = (ord(c)-ord(first)) % 26
                key.append(digit)
            return tuple(key)
                
        out = collections.defaultdict(list)
        for s in strings:
            key = computeKey(s)
            out[key].append(s)
        return list(out.values())

print(Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z", "cegh"]))