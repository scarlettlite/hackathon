from collections import defaultdict
class Solution:
    def __init__(self):
        self.trie = {}
        self.cache = defaultdict(list)

    def insert(self, word):
        curr = self.trie
        if word == "":
            return
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr["*"] = True

    def search(self, word):
        if word == "":
            return False
        curr = self.trie
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        if curr.get('*', None) == True:
            return True
        return False

    def insertWords(self, words):
        for word in words:
            self.insert(word)

    def findBreaks(self, s):
        n = len(s)
        for i in range(1, n+1):
            for j in range(0,i):
                x, y = s[:j], s[j:i]
                isxfound, isyfound = self.search(x), self.search(y)
                if self.cache.get((0,j), None) and isyfound == True:
                    for t in self.cache.get((0,j), None):
                        self.cache[(0,i)].append(t + " " + y)
                elif isxfound == True and isyfound == True:
                    self.cache[(0,i)].append(x+ " " +y)
                elif x == "" and isyfound == True:
                    self.cache[(0,i)].append(y)
        return self.cache[(0,n)]
                

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.insertWords(wordDict)
        return self.findBreaks(s)

print(Solution().wordBreak("catbatratbatratdid", ["cat", "bat", "rat", "did", "catbat", "batrat", "ratdid"]))