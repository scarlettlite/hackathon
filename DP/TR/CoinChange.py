"""
Given an infinite supply of coins find out the minimum 
number of coins of making a change for amount x
assume you have infinite amount of coins
"""
class Solution:
    def mincoins(self, coins, amount):
        if not coins: return 0
        n = len(coins)
        dp = [0 if i == 0 else float('inf') for i in range(amount+1)]
        sol = [-1 for i in range(amount+1)]
        for i,x in enumerate(coins):
            for j in range(amount + 1):
                if j >= x:
                    if 1+dp[j-x] < dp[j]:
                        dp[j] = 1+dp[j-x]
                        sol[j] = i
        ans = self.printSolution(sol, amount, coins)
        return dp[-1], ans

    def printSolution(self, sol, amount, coins):
        ans = []
        while amount > 0:
            x = coins[sol[amount]]
            ans.append(x)
            amount -= x
        return ans


p,q = Solution().mincoins([7,2,3,6], 13)

