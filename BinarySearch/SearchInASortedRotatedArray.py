class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return False
        
        lo = 0
        hi = len(nums) - 1 
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= nums[hi]:
                hi = mid
            else:
                lo = mid + 1

        if target > nums[-1]:
            lo = 0
            hi -= 1
        else:
            hi = len(nums) - 1
            
        while lo <= hi:
            mid = (lo + hi) // 2
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                return True
            
        return False

print(Solution().search([1,1,3,1],3))