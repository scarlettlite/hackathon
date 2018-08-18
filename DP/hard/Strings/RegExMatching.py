class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        dp = [[False for _ in range(m+1)] for _ in range(n+1)]
        dp[0][0] = True
        for i in range(2,m+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j] 
        return dp[-1][-1]

print(Solution().isMatch("aa", "a*")) 
