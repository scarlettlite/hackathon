class Solution:
    def helper(self, nums, i):
        if i == len(nums):
            self.ans.add(tuple(nums))
        else:
            for j in range(i,len(nums)):
                nums[i], nums[j] = nums[i], nums[j]
                self.helper(nums, i+1)
                nums[i], nums[j] = nums[i], nums[j]
        
        
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = set()
        self.helper(nums, 0)
        return [list(x) for x in self.ans]