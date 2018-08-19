class Solution:
    def preprocess(self, nums):
        i, j, n = 0, 1, len(nums)
        while j < n :
            if nums[j] == nums[j-1]:
                while i < n and nums[i] == nums[j] and ((i > 0 and nums[i-1] != nums[j]) or (i < n-1 and nums[i+1] != nums[j])):
                    i += 1
                if i < n and nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
            j += 1

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #self.preprocess([4,5,6,1,1,1,1])

print(Solution().preprocess([4,5,6,1,1,1,1]))
        