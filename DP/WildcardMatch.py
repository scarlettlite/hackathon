class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        #handle patterns like ***y, r**b
        x = ""
        a = -1
        while a < len(p):
            a +=1
            if a > 0 and p[a-1] == "*" and p[a] == "*":
                continue
            x += p[a]
        p = x
        n = len(s)+1 #Add 1 for empty string
        m = len(p)+1 #Add 1 for empty string
        dp = [[False for _ in range(m)] for _ in range(n)]
        dp[0][0] = True
        #if first character of the pattern is * then * matches an empty string
        if p and p[0] == '*':
            dp[0][1] = True
        for i in range(1,n):
            for j in range(1,m):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                """
                indices shifted backwards due to empty string
                if * matches an empty string then match t[:i] with p[:j-1]
                if * matches the current character then match [t:i-1] with p[:j]
                """
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return dp[-1][-1]

print(Solution().isMatch("hell", "****hell"))