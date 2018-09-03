class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            j = nums[i]
            while j != nums[j-1]:
                nums[j-1] , j = j, nums[j-1]

        ans = []
        for i,x in enumerate(nums):
            if i+1 != x:
                ans.append(i+1)
        return ans

print(Solution().findDisappearedNumbers([1,1,1,1]))
