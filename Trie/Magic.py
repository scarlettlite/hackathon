import collections
class MagicDictionary(object):
    def _genneighbors(self, word):
        for i in xrange(len(word)):
            yield word[:i] + '*' + word[i+1:]

    def buildDict(self, words):
        self.words = set(words)
        self.count = collections.Counter(nei for word in words
                                        for nei in self._genneighbors(word))

    def search(self, word):
        return any(self.count[nei] > 1 or
                self.count[nei] == 1 and word not in self.words
                for nei in self._genneighbors(word))    
# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(["hello","leetcode", "hallo"])
# print(obj.search("hhllo"))
# print(obj.search("hhelo"))
# print(obj.search("hello"))
# print(obj.search("hell"))
# print(obj.search("leetcoded"))

print(obj.search("hhllo"))