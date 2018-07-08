class Solution:
    def __init__(self):
        self.root = {}
        
    def createtrie(self, words):
        for i, word in enumerate(words):
            curr = self.root
            for ch in reversed(word):
                curr = curr.setdefault(ch, {})
            curr['value'] = i
            
    def getwords(self, prefix):
        curr = self.root
        for ch in prefix:
            if curr.get(ch) == None:
                return []
            curr = curr.get(ch)
        return self.traverse(curr)
    
    def traverse(self, curr):
        result = []
        for key, value in curr.items():
            if key == 'value':
                result.append(value)
            else:
                result.extend(self.traverse(value))
        return result
    
            
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        self.createtrie(words)
        ans = []
        for i, word in enumerate(words):
            matches = self.getwords(word)
            for x in matches:
                pal = word + words[x]
                if pal == pal[::-1] and i != x:
                    ans.append([i, x])
        return ans
        

print(Solution().palindromePairs(["a", ""]))