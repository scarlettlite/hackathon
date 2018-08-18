class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        first, second = float('-inf'), float('-inf')
        fi = - 1
        for i,x in enumerate(nums):
            if second <= first <= x:
                second = first
                first = x
                fi = i
            elif second <= x <= first:
                second = x
        if 2*first >= second:
            return fi
        return -1

print(Solution().dominantIndex([1,2,3,4]))