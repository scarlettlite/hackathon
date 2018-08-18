class Solution(object):
    def dfs(self, grid, r, c, visited):
        area = 0
        if (r,c) not in visited and grid[r][c]  == 1:
            visited.add((r,c))
            area = 1
            for ir,ic in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= ir < len(grid) and 0 <= ic < len(grid[ir]):
                    area += self.dfs(grid, ir, ic, visited)
        return area



    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        if not grid: return 0
        mv, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                mv = max(mv, self.dfs(grid, i, j, visited))
        return mv


print(Solution().maxAreaOfIsland([[]]))