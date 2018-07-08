class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices : return 0
        n = len(prices)
        ans = 0
        dp = [[0 for _ in range(n)] for _ in range(n)]
        minarray = [x for x in prices]
        value = minarray[-1]
        for i in range(n-2, -1, -1):
            if minarray[i] > value:
                minarray[i] = value
            else:
                value = minarray[i]
        for i in range(n):
            for j in range(n):
                if i<j:
                    dp[i][j] = max(dp[i][j-1], prices[j] - minarray[i])
        ans = dp[0][n-1]
        for i in range(n-1):
            ans = max(ans, dp[0][i] + dp[i+1][n-1])
        return ans
        
print(Solution().maxProfit([3,3,5,0,0,3,1,4]))