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
            if ch == None:
                return []
        return self.traverse(curr)

sol = Solution()
sol.createtrie(['apple', 'apply', 'apt', 'applicant', 'sane', 'sanity' ,'sad'])

print(sol.getwords('app'))
print(sol.getwords('ap'))
print(sol.getwords('sa'))
#print('yes')

