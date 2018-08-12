from bisect import bisect, insort
class Solution:
    def getmedian(self, nums):
        n = len(nums)
        x, y = nums[n//2 - 1], nums[n//2]
        if n & 1:
            return float(y)
        else:
            return float(x + y) / 2
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if k == 0: return []
        if k == 1: return nums
        medians, arr = [], nums[:k]
        arr.sort() 
        for i in range(k, len(nums) + 1):
            medians.append(self.getmedian(arr))
            arr.pop(bisect(arr, nums[i-k]) - 1)
            if i < len(nums): insort(arr, nums[i])
        return medians

# [1,-1,-1,3,5,6]
print(Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


            

