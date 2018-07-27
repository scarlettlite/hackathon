"""
Given an array of repeated numbers generate all unique permutations
"""

class Solution:
    def helper(self, nums, i):
        if i == len(nums):
            self.ans.append(nums[:])
        else:
            seen = set()
            for j in range(i,len(nums)):
                if nums[j] in seen:
                    continue
                else:
                    seen.add(nums[j])
                    nums[i], nums[j] = nums[j], nums[i]
                    self.helper(nums, i+1)
                    nums[i], nums[j] = nums[j], nums[i]
        
        
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        self.helper(nums, 0)
        return self.ans

print(Solution().permuteUnique([1,2,3]))