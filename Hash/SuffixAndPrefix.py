from collections import defaultdict
class WordFilter:
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.ss = defaultdict(set)
        self.pp = defaultdict(set)
        self.ww = { x:i for i,x in enumerate(words)}
        for i, word in enumerate(words):
            for i in range(0, len(word)+1):
                self.ss[word[i:]].add(word)
                self.pp[word[:i]].add(word)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        candidates = self.pp[prefix] & self.ss[suffix]
        return max([-1] + [self.ww[c] for c in candidates])

"""
Trie Implementation
"""
Trie = lambda: defaultdict(Trie)
WEIGHT = False

class WordFilterTrie(object):
    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            conj = word + '#' + word
            for i in range(len(word)+1):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, len(conj)):
                    cur = cur[conj[j]]
                    cur[WEIGHT] = weight

    def f(self, prefix, suffix):
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]



wf = WordFilterTrie(['apple', 'ate', 'attic', 'enumerate'])   
print(wf.f('a','e'))
print(wf.f('x','e'))
print(wf.f('','e'))
print(wf.f('a',''))
print(wf.f('',''))

        
