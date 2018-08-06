"""
https://leetcode.com/problems/maximum-distance-in-arrays/
"""

class Solution:
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        val = list()
        for i,arr in enumerate(arrays):
            mi, ma = float('inf'), float('-inf')
            for x in arr:
                mi = min(mi, x)
                ma = max(ma, x)
            val.append((mi,i))
            val.append((ma,i))
        val.sort()
        i, j = 0, len(val) - 1
        ans = 0
        if val[i][1] == val[j][1]:
            ans = max(val[j][0]-val[i+1][0], abs(val[j-1][0]-val[i][0]))
        else:
            ans = val[j][0] - val[i][0]
        return ans

print(Solution().maxDistance([[1,2,3],[4,5,6,9]]))