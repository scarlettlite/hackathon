class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        maxprofit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                maxprofit += prices[i] - prices[i-1]
        return maxprofit

Solution().maxProfit([1,4,6,8,10,15])