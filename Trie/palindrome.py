class Solution:
    def __init__(self):
        self.root = {}
        
    def createtrie(self, words):
        for i, word in enumerate(words):
            if word != '':
                curr = self.root
                for ch in reversed(word):
                    curr = curr.setdefault(ch, {})
                curr['value'] = i

    def ispalindrome(self, word):
        return word and word == word[::-1]
            
    def getwords(self, prefix):
        matches = []
        curr = self.root
        """
        #Tricky:
        1) Check if any reversed word begins with a prefix 
            -> this will try to match the largest possible prefix
            -> ispalindrome (prefix + match)
        2) Also match a prefix if (prefix[:i] + ispalindrome(prefix[i+1:]) + palindrome(prefix[:i]))
        """
        for i, ch in enumerate(prefix):
            if curr.get(ch) != None:
                curr = curr.get(ch)
                a = self.ispalindrome(prefix[i+1:])
                b = curr.get('value')
                if a and b != None:
                    matches.append(curr.get('value'))
        matches.extend(self.traverse(curr))
        return matches
    
    def traverse(self, curr):
        if curr == None : []
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
        ans = set()
        for i, word in enumerate(words):
            if word == '':
                continue
            matches = self.getwords(word)
            for x in matches:
                pal = word + words[x]
                if pal == pal[::-1] and i != x:
                        ans.add((i, x))
        ans = [[i,x] for i,x in ans]
        if '' in words:
            j = words.index('')
            for i,word in enumerate(words):
                if word == word[::-1] and i != j:
                    ans.append([i,j])
                    ans.append([j,i])
        return ans
        
print(Solution().palindromePairs(["a", "aa"]))