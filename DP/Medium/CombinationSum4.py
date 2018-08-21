class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(1, target+1):
            k = 0
            while k < len(nums) and nums[k] <= j:
                dp[j] += dp[j-nums[k]]
                k += 1
        return dp[-1]

print(Solution().combinationSum4([1,2,3], 4))