class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums = sorted(nums)
        count = 0
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    count += (r-l)
                    l += 1
                else:
                    r -= 1
        return count

print(Solution().threeSumSmaller([-2,0,1,3], 2))
