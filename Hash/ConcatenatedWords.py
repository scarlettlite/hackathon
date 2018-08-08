"""
this question required a true or false
instead of a list. Evaluate every decision for 
coding before actually coding"""

class Solution:
    def __init__(self):
        self.words = set()

    def helper(self, word, i):
        if i == len(word):
            return True
        else:
            for j in range(i+1, len(word)+1):
                if word[i:j] in self.words:
                    if self.helper(word, j) == True:
                        return True
        return False
                    
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=lambda x:len(x))
        ans = []
        for w in words:
            if not w: continue
            if self.helper(w, 0) == False:
                self.words.add(w)
            else:
                ans.append(w)
        return ans

