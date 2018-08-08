import heapq
from functools import cmp_to_key
class Trie:
    def __init__(self):
        self.node = {}
        self.wl = []

def cmp(l1, l2):
    if l1[0] == l2[0]:
        for a,b in zip(l1[1], l2[1]):
            if a != b:
                return ord(b) - ord(a)
        else:
            return len(l2[1]) - len(l1[1])
    else:
        return l1[0] - l2[0]

        
class AutocompleteSystem:

    def insert(self, sentence, times):
        if sentence == '':
            return
        curr = self.trie
        st = [times, sentence]
        for x in sentence:
            if curr.node.get(x, None) == None:
                curr.node[x] = Trie()
            curr.wl.append(st)
            curr = curr.node[x]
        curr.wl.append(st)

    def find(self, prefix, curr):
        if not prefix: return []
        for x in prefix:
            if curr.node.get(x, None) == None:
                self.curr = None
                return []
            curr = curr.node[x]
        self.curr = curr
        return curr.wl

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Trie()
        self.curr = self.trie
        self.inp = ""
        for s,t in zip(sentences, times):
            self.insert(s,t)
        
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        curr = self.curr
        heap = []
        if c == '#':
            if self.curr and self.curr.wl:
                for x in self.curr.wl:
                    x[0] += 1
            else:
                self.insert(self.inp, 1)
            self.inp = ""   
            self.curr = self.trie
        else:
            self.inp += c
            curr = self.curr
            if curr != None :heap = self.find(c, curr)
        y = heapq.nlargest(3, heap, key=cmp_to_key(cmp))
        return [x[1] for x in y]