class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None:
            return -1
        if s == "":
            return 0
        n = len(s)
        palin = [[False for j in range(n)] for i in range(n)]
        cuts = list(range(n)) 
        for j in range(n): 
            for l in range(1, j + 2): # substring length
                i = j + 1 - l
                if s[i] == s[j] and (j-i <= 1 or palin[i+1][j-1] == True):
                    palin[i][j] = True
                    if i == 0:
                        cuts[j] = 0
                    elif cuts[j] > cuts[i - 1] + 1:
                        cuts[j] = cuts[i - 1] + 1
        return cuts[-1]

print(Solution().minCut("abba"))
