"""
Given a set of coins and an amount find the number of
ways you can make change to get the specified amount
assume that infinite supply of each denomination
"""

class Solution:
    def coinsways(self, coins, amount):
        n = len(coins)
        dp = [[ 0 for j in range(amount+1)] for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]
                if j >= coins[i-1]:
                    dp[i][j] += dp[i][j-coins[i-1]]
        return dp[-1][-1]

Solution().coinsways([1,2,3], 5)

            



