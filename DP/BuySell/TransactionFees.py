class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        if not prices:
            return 0

        buy = [0 for _ in range(n)]
        sell = [0 for _ in range(n)]
        buy[0] = -prices[0]

        for i in range(1, n):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i] - fee)
        return sell[-1]

print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))