"""
Solution with best explanation
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
"""

class Solution:
    def maxProfitHelper(self, prices, m):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices : return 0
        n = len(prices)+1
        prices = [0] + prices
        m = m+1
        dp = [[0 for _ in range(n)] for _  in range(m)]
        for i in range(1,m):
            mv = prices[1]
            for j in(range(2,n)):
                mv = min(mv, prices[j] - dp[i-1][j-1])
                dp[i][j] = max(dp[i][j-1], prices[j] - mv)
        return dp[-1][-1]

    def maxProfit(self, prices):
        return self.maxProfitHelper(prices, 2)


        
print(Solution().maxProfit([1,4,5,1,7,5,6]))