class Solution:
    def __init__(self):
        self.cache = {}
    def helper(self, nums, i, ss, target):
        ans = 0
        n = len(nums)
        if i == n and ss == target:
            ans = 1
        elif i < n:
            if self.cache.get((i,ss), None) == None:
                ans += self.helper(nums, i+1, ss + nums[i], target)
                ans += self.helper(nums, i+1, ss - nums[i], target)
                self.cache[(i,ss)] = ans
            else:
                ans = self.cache[(i,ss)]

        return ans

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.helper(nums, 0, 0, S)

print(Solution().findTargetSumWays([1,1,1,1,1,1,2,3], 4))
