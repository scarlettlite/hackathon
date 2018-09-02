"""https://leetcode.com/problems/shortest-path-to-get-all-keys/"""
from collections import deque
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
        pq =  deque([(sr,sc,0,".@abcdef",0)])
        m,n = len(grid), len(grid[0])
        seen = {(sr,sc,"","")}
        direc = [[0,1],[0,-1],[1,0],[-1,0]]
        while pq:
            r,c,d,keys,found = pq.popleft()
            if grid[r][c] in 'abcdef' and grid[r][c].upper() not in keys: 
                keys += grid[r][c].upper()
                found += 1
            if found == ck:
                return d
            for di, dj in direc:
                ir, ic = r + di, c + dj
                if 0 <= ir < m  and 0 <= ic < n and grid[ir][ic] in keys:
                    if (ir,ic,keys) not in seen:
                        seen.add((ir,ic,keys))
                        pq.append((ir,ic,d+1,keys,found))
        return -1


print(Solution().shortestPathAllKeys(["@.CaA","..B#.",".c..b"]))   


                