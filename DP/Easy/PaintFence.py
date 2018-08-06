"""
https://leetcode.com/problems/paint-fence
"""
class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return k
        same, diff = k, k*(k-1)
        for _ in range(3, n+1):
            same, diff = diff, (same + diff)*(k-1)
        return same + diff

print(Solution().numWays(3,2))