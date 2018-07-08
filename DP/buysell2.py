class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        profit = 0
        bp = prices[0]
        cm = 0
        sp = prices[0]
        for x in prices[1:]:
            print(bp,sp,cm,profit)
            if x < sp:
                cm = 0
                bp = x
                sp = x
            if x > bp:
                pm = cm
                cm = max(pm, x-bp)
                sp = x
                if pm < cm:
                    profit += (cm - pm)
        return profit

Solution().maxProfit([1,4,6,8,10,15])