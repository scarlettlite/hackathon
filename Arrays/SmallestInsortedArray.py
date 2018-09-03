class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minvalue, maxvalue = float('inf'), float('-inf')
        n = len(nums)
        for i in range(1,n):
            if nums[i-1] > nums[i]:
                minvalue = min(minvalue, nums[i])
        for i in range(n-1,0,-1):
            if nums[i] < nums[i-1]:
                maxvalue = max(maxvalue, nums[i-1])
        for l in range(n):
            if nums[l] > minvalue:
                break
        for r in range(n-1,-1,):
            if nums[r] < maxvalue:
                break
        return r - l + 1 if r > l else 0
