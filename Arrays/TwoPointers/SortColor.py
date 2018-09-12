"""
idea is to partition array around 1
"""

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        sz = len(nums)
        left, right = -1, sz
        ind = 0
        while ind < right:
            if nums[ind] == 0:
                left += 1
                nums[left], nums[ind] = nums[ind], nums[left]
                if left == ind: 
                    ind += 1
            elif nums[ind] == 2:
                right -= 1
                nums[right], nums[ind] = nums[ind], nums[right]
            elif nums[ind] == 1:
                ind += 1

print(Solution().sortColors([2,0,2,1,1,0]))



        

print(Solution().sortColors([2,0,1]))