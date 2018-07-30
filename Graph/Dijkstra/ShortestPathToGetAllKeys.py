"""https://leetcode.com/problems/shortest-path-to-get-all-keys/"""

import heapq
class Solution:
    def getstartingpoint(self, grid):
        sc, sr = -1,-1
        ck = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                x = grid[i][j]
                if x == '@':
                    sr, sc = i,j
                if x.isalpha() and x.islower():
                    ck+=1

        return sr, sc, ck

    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        if not grid: return -1
        sr, sc, ck = self.getstartingpoint(grid)
        pq =  [(0, sr, sc)]
        m,n = len(grid), len(grid[0])
        seen, keys, ans = set((0,0)), set(), -1
        while pq:
            d, r, c = heapq.heappop(pq)
            y = grid[r][c]
            if y.islower():
                ans = d
            for ir, ic in ((r,c+1), (r,c-1), (r-1,c), (r+1,c)):
                if 0 <= ir < m and 0 <= ic < n and (ir, ic) not in seen:
                    x = grid[ir][ic]
                    if x == '.':
                        heapq.heappush(pq, (d+1, ir, ic))
                        #seen.add((ir, ic))
                    if x.islower() :
                        heapq.heappush(pq, (d+1, ir, ic))
                        keys.add(x)
                        #seen.add((ir, ic))
                    if x.isupper() and x.lower() in keys:
                        heapq.heappush(pq, (d+1, ir, ic))
                        #seen.add((ir, ic))
        if ck != len(keys):
            ans = -1
        return ans

print(Solution().shortestPathAllKeys(["@.CaA","..B#.",".c..b"]))   


                