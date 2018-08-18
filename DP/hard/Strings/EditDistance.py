"""
Find the minimum edit distance between two strings
"""
class Solution:
    def editDistance(self, a, b):
        m = len(a)+1
        n = len(b)+1
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(0,m):
            dp[i][0] = i
        for j in range(0,n):
            dp[0][j] = j  
        for i in range(1,m):
            for j in range(1,n):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        print(self.printSol(dp,a,b))
        return dp[-1][-1]
    
    def printSol(self, dp, a, b):
        i, j = len(dp)-1, len(dp[0]) -1
        ans = []
        while i > 0 and j > 0:
            if a[i-1] == b[j-1] and dp[i][j] == dp[i-1][j-1]:
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i-1][j] + 1:
                """
                delete a character from a to calculate the
                edit distance
                """
                ans.append("delete " + a[i-1])
                i -= 1
            elif dp[i][j] == dp[i-1][j-1] + 1:
                ans.append("replace "+ a[i-1]+ ' with '+ b[j-1])
                i -= 1
                j-= 1
            elif dp[i][j] == dp[i][j-1] + 1:
                """
                insert a character in a to calculate the edit 
                distance
                """
                ans.append("insert "+ a[i-1])
                j -= 1
        return ans[::-1]
        

p = Solution().editDistance("abcdef", "azced")
    