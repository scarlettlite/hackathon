class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        ans = []

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            l = i + 1
            r = n - 1
            while l < r:
                ss = nums[i] + nums[l] + nums[r]
                if ss == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
                elif ss < 0:
                    l += 1
                else:
                    r -= 1
        return ans

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))