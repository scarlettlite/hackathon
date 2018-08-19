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
        for s in range(n-2, -1, -1):
            for e in range(s+1, n):
                dp[s][e] = max(nums[s] - dp[s+1][e], nums[e] - dp[s][e-1])
        return dp[0][-1] >= 0

print(Solution().PredictTheWinner([1,5,2,4,6]))