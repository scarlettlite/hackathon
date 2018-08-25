class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        closest = nums[0] + nums[1] + nums[-1]
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                ns = nums[i] + nums[l] + nums[r]
                if abs(closest - target) > abs(ns - target):
                    closest = ns
                if ns == target:
                    return target
                elif ns < target:
                    l += 1
                else:
                    r -= 1
        return closest



print(Solution().threeSumClosest([-1, 2, 1, -4], 1))