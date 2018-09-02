class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0] : return 0
        m,n = len(grid), len(grid[0])
        rowhits = 0
        colhits = [0]*n
        maxvalue = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    continue
                if j == 0 or grid[i][j-1] == 'W':
                    rowhits = self.rowenemies(grid, i, j)
                if i == 0 or grid[i-1][j] == 'W':
                    colhits[j] = self.colenemies(grid, i, j)
                if grid[i][j] == '0':
                    maxvalue = max(maxvalue, rowhits + colhits[j])
        return maxvalue

    def colenemies(self, grid, i, j):
        m, count = len(grid), 0
        while i < m and grid[i][j] != 'W':
            if grid[i][j] == 'E':
                count += 1
            i += 1
        return count

    def rowenemies(self, grid, i, j):
        n, count = len(grid[0]), 0
        while j < n and grid[i][j] != 'W':
            if grid[i][j] == 'E':
                count += 1
            j += 1
        return count





print(Solution().maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]])) 