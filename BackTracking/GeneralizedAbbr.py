class Solution:
    def helper(self, word):
        if word == "":
            return [""]
        else:
            n = len(word)
            ans = []
            for l in range(n, 0, -1):
                for i in range(0, n-l+1):
                    j = i+l
                    dig, em = str(j-i), ""
                    prefix  = word[:i]
                    if j < n:
                        em = word[j]
                    mid = dig + em
                    suffixes =  self.helper(word[j+1:])
                    for s in suffixes:
                        ans.append(prefix + mid + s)
            return ans + [word]


            
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        return self.helper(word)

print(Solution().generateAbbreviations('word'))
#["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]