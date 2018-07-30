"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
"""
from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        c3 = c1 & c2
        return list(c3)

print(Solution().intersect([1,1,2,2], [2,2]))