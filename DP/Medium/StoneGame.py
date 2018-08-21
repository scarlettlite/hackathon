"""
https://leetcode.com/problems/predict-the-winner/
https://leetcode.com/problems/stone-game/
"""
class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0 for i in range(n)] for j in range(n)]
        for l in range(2,n+1):
            for s in range(0, n-l+1):
                e = s + l - 1
                dp[s][e] = max(nums[s] - dp[s+1][e], nums[e] - dp[s][e-1])
        return dp[0][-1] >= 0

print(Solution().PredictTheWinner([1,5,2,4,6]))