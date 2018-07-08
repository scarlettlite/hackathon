class Solution:
    def __init__(self):
        self.trie = {}
        self.results = []
        
    def createtrie(self, words):
        for word in words:
            curr = self.trie
            for ch in word:
                curr = curr.setdefault(ch, {})
            curr['value'] = word
    
    def traverse(self, tree):
        result = []
        for key, value in tree.items():
            if key == 'value':
                result.append(value)
            else:
                result += self.traverse(value)
        return result
            
                
    def getwords(self, prefix):
        curr = self.trie
        for ch in prefix:
            curr = curr.get(ch)
            if curr == None:
                return []
        return self.traverse(curr)
    
    def iswordsquare(self, square):
        for i in range(len(square)):
            for j in range(len(square)):
                if square[i][j] != square[j][i]:
                    return False
        else:
            return True
                
    def getprefix(self, square, k):
        prefix = ""
        for i in range(0,k):
            prefix += square[k][i]
        return prefix
            
    def putword(self, square, k, word):
        for i, ch in enumerate(word):
            square[k][i] = ch
            square[i][k] = ch
            
    def reset(self, square, k):
        for i in range(len(square)):
            if i >= k:
                square[k][i] = None
                square[i][k] = None
            
    def backtrack(self, square, k, wordsin, word):
        self.putword(square, k, word)
        if k == len(square) - 1:
            if self.iswordsquare(square):
                self.results.append([''.join(row) for row in square])
                self.reset(square, k)
            return
        prefix = self.getprefix(square, k+1)
        candidates = filter(lambda x: x != word, self.getwords(prefix))
        for candidate in candidates:
            self.backtrack(square, k+1, wordsin, candidate)
        self.reset(square, k)
        
        
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        square = [[None for _ in range(len(words[0]))] for _ in range(len(words[0]))]
        self.createtrie(words)
        for word in words:
            self.backtrack(square, 0, [], word)
        return self.results


print(Solution().wordSquares(["abat","baba","atan","atal"]))