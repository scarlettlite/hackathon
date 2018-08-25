class Solution:
    """
    Check whether target exists in nums or not
    if it exists return its index otherwise return -1
    """
    def binarySearch(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid -1
        if 0 <= lo <= len(nums) -1:
            return lo
        return -1


    def nextGreaterValue(self, nums, target):
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
        return nums[lo%n]


    def nextSmallerValue(self, nums, target):
        n = len(nums)
        lo, hi = 0, n - 1
        while hi - lo < 2:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid
        #ans can be any one of lo or hi
        if abs(nums[hi] - target) < abs(nums[lo] - target):
            lo = hi
        return nums[lo%n]
