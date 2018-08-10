class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dd, ss, count = {0:1}, 0, 0
        for x in nums:
            ss += x
            c = dd.get(ss-k, None)
            if c != None:
                count += c
            if ss not in dd:
                dd[ss] = 0
            dd[ss] += 1
        return count

print(Solution().subarraySum([2,2,1,2,1,2], 3))