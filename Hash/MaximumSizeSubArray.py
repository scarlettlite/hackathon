class Solution:
    def maxSubArrayLen(self, nums, k):
        index, l, sm = {}, 0, 0
        """
        if some subarray adds up to zero,
        then include it
        """
        index[0] = -1
        for i, num in enumerate(nums):
            sm += num
            """
            sm - (sm - k) = k 
            """
            if sm - k in index:
                l = max(l, i - index[sm - k])
            if sm not in index:
                """
                for each sum note the earliest index at which the sum occurs
                """
                index[sm] = i
        return l

print(Solution().maxSubArrayLen([-2, -1, 2, 1], 1))