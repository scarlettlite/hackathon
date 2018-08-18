class Solution:
    def preprocess(self, nums):
        i, j, n = 0, 1, len(nums)
        while j < n :
            if nums[j] == nums[j-1]:
                i = (j+1)%n
                while i % n != j-1 and nums[i] == nums[j]:
                    i = (i+1) % n
                if i % n != j-1 and nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
            j += 1

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.preprocess([4,5,6,1,1,1,1])

print(Solution().preprocess([1,1,1,1,4,5,6]))
        