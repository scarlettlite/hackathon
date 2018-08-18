import numpy as np
class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        dp = [[float("inf") for _ in range(n+1)] for _ in range(m+1)]
        csum = np.cumsum([0]+nums) 
        dp[0][0] = 0
        """
        @rathor: write the explanation next week
        """
        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(0, j):
                    dp[i][j] = min(dp[i][j], max(dp[i-1][k], csum[j] - csum[k]))
        return dp[-1][-1]


print(Solution().splitArray([7,2,5,10,8], 2))