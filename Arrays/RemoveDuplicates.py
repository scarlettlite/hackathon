class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = nl = len(nums)
        nl = 0 
        j = i = 0
        while j < n:
            while j < n and nums[j] == nums[i]:
                j += 1
            if j < n:
                nums[i+1] = nums[j]
            i += 1
            nl += 1
        return nl
print(Solution().removeDuplicates([0,0,0,0,1,1,1,1,4,6,6,7,7,7]))