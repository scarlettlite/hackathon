from collections import defaultdict
class Solution:
    def __init__(self):
        self.cache = defaultdict(list)
        self.ans = []

    def populateCache(self, s, wordDict):
        n = len(s)
        wordDict = set(wordDict)
        self.cuts = [False] * (n + 1)
        self.cuts[0] = True
        for i in range(0, n+1):
            for j in range(i):
                rst = self.cuts[j] and s[j:i] in wordDict
                if rst:
                    self.cuts[i] = True
                    self.cache[j].append(i)

    def findBreaks(self, path, index, s):
        if index == len(s):
            self.ans.append(' '.join(path))
        else:
            for x in self.cache[index]:
                path.append(s[index:x])
                self.findBreaks(path, x, s)
                path.pop()

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.populateCache(s, wordDict)
        if self.cuts[-1] == True:
            self.findBreaks([], 0, s)
        return self.ans

print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))