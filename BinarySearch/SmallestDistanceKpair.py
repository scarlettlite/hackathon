class Solution(object):
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                """
                Note the asymmetry while updating low and high
                is it because of work repeated values and less than equal to
                as opposed less than 
                """
                lo = mi + 1

        return lo


print(Solution().smallestDistancePair([1,7,2,5,7,8,7,7], 5))