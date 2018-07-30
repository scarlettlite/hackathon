"""
https://leetcode.com/problems/swim-in-rising-water/
"""
"""
The most important point to note in this problem 
"""
import heapq
class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        seen = set()
        pq = [(grid[0][0], 0, 0)]
        N = len(grid)
        ans = 0
        while pq:
            d,r,c = heapq.heappop(pq)
            ans = max(d, ans)
            if r == N-1 and c == N-1:
                break
            for ir, ic in ((r,c-1), (r,c+1), (r+1,c), (r-1,c)):
                if 0 <= ir <= N-1 and 0 <= ic <= N-1 and (ir,ic) not in seen:
                    heapq.heappush(pq, (grid[ir][ic], ir, ic))
                    seen.add((ir,ic))
        return ans
        
print(Solution().swimInWater([[0,2],[1,3]]))          

        