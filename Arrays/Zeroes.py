class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero, nonzero = 0,0
        n = len(nums)
        while nonzero < n and zero < n:
            while zero < n and nums[zero] != 0:
                zero += 1
            while nonzero < n and nums[nonzero] == 0:
                nonzero += 1
            if zero < n and nonzero < n and zero < nonzero:
                nums[nonzero], nums[zero] = nums[zero], nums[nonzero]
            nonzero += 1
        return nums

print(Solution().moveZeroes([0,1,0,0,0,3,5,6,0,0,9]))