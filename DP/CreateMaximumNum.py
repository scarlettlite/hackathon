class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums1 = [(x,i) for i,x in enumerate(nums1)]
        nums2 = [(x,i) for i,x in enumerate(nums2)]
        nums = list(nums1, nums2)
        for 