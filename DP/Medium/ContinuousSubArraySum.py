class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ss = 0
        cache = {0:-1}
        for i,x in enumerate(nums):
            ss = (ss+x) % k 
            if ss not in cache:
                cache[ss] = i
            elif i - cache[ss] > 1:
                return True
            else:
                cache[ss] = i
        return False

print(Solution().checkSubarraySum([7, 1, 1, 1, 14, 5,2], 7))