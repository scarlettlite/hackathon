class Solution:
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if not N: return 0
        n = N+1
        dp = [ 1 if i == 1 else 0 for i in range(n)]
        for i in range(2, n):
            dp[i] = dp[i-1] + 1
            if i > 3:
                for k in range(3, i):
                    x = dp[i-k] * (k-1)
                    dp[i] = max(dp[i], x)
        return dp[-1]

print(Solution().maxA(10))
