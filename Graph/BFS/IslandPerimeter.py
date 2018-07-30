from collections import deque

class Solution:
    def getstart(self, grid):
        m = len(grid)
        for i in range(m):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return i, j
        return -1, -1,
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s = self.getstart(grid)
        queue = deque([s])
        seen = set([s])
        peri = 0
        while queue:
            r,c = queue.popleft()
            p = 4
            for ir, ic in ((r,c-1), (r,c+1), (r-1,c), (r+1,c)):
                if 0 <= ir < len(grid) and 0 <= ic < len(grid[ir]):
                    x = grid[ir][ic]
                    if x == 1:
                        if (ir, ic) not in seen:
                            queue.append((ir, ic))
                            seen.add((ir, ic))
                        p -= 1
            peri += p
    
        return peri

print(Solution().islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))