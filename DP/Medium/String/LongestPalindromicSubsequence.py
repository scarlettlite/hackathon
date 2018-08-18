"""
Find the longest Palindromic subsequence in a String
"""
class Solution:
    def lps(self, a):
        n = len(a)
        dp = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        for l in range(2, n+1):
            for i in range(0, n-l+1):
                j = i+l-1
                if a[i] == a[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        x, y = "", ""
        i = 0
        j = n-1
        while i <= j:
            if (dp[i][j] == 2 + dp[i+1][j-1] and a[i] == a[j] or i == j):
                x+=a[i]
                if i < j:
                    y = a[i] + y
                i += 1
                j -= 1
            elif dp[i][j] == dp[i-1][j]:
                i += 1
            else:
                j -= 1
        print(x+y)

        return dp[0][-1]


Solution().lps("agbdgda")