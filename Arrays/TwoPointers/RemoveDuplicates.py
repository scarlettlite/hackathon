
"""https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/"""
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return nums
        n = len(nums)
        oid,nid = 0,0
        while oid < n:
            count = 1
            x = nums[oid]
            while oid+1 < n and nums[oid] == nums[oid+1]:
                oid += 1
                count += 1
            if count == 1:
                nums[nid] = x
                nid += 1
            elif count >= 2:
                nums[nid], nums[nid+1] = x, x
                nid += 2
            oid += 1
        return nid

print(Solution().removeDuplicates([0,0,0,1,1,1,2,2,2,2,3]))
