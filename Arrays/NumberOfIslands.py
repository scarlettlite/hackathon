class Solution(object):
    def dfs(self, grid, r, c, visited):
        if (r,c) not in visited and grid[r][c]  == '1':
            visited.add((r,c))
            for ir,ic in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= ir < len(grid) and 0 <= ic < len(grid[ir]):
                    self.dfs(grid, ir, ic, visited)
            return True
        return False

    def numIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        if not grid: return 0
        count, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(grid, i, j, visited) == True:
                    count += 1
        return count


print(Solution().numIslands([[]]))