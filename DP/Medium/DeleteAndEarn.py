from collections import Counter
class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        avoid, using = 0, 0
        prev = None
        for k in sorted(c):
            if k-1 == prev:
                avoid, using = max(avoid, using), k * c[k] + avoid
            else:
                avoid, using = max(avoid, using), k * c[k] + max(avoid, using)
            prev = k
        return max(avoid, using)

print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]))