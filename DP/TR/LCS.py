"""
Given two strings find the longest common subsequence
between the two strings
"""

class Solution:
    def lcs(self, a,b):
        m = len(a)
        n = len(b)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print("".join(self.printSol(dp,a,b)))
        return dp[-1][-1]

    def printSol(self, dp, a, b):
        i = len(dp) - 1
        j = len(dp[0]) - 1
        ans = []
        while i > 0 and j > 0:
            if dp[i][j] == 1+dp[i-1][j-1] and a[i-1] == b[j-1]:
                ans.append(a[i-1])
                i-=1
                j-=1
            elif dp[i][j] == dp[i-1][j]:
                i -= 1
            else:
                j -= 1
        return ans[::-1]

p = Solution().lcs("asdfgh", "ahdfsg")
