class Solution:
    def minSubArrayLen(self, k, nums):
        if not nums: return 0
        left, ans, ss = 0, len(nums), 0
        for i,x in enumerate(nums):
            ss += x
            while ss >= k:
                ans = min(ans, i - left + 1)
                ss -= nums[left]
                left += 1
        return ans

print(Solution().minSubArrayLen(7, [2,6, 10]))