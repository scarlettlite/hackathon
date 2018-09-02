from heapq import heappop, heappush
class Solution:
    def shortestDistance(self, maze, start, destination):
        start, destination = tuple(start), tuple(destination)
        queue = [((0,) + start)]
        visited = { start:0 }
        m, n = len(maze), len(maze[0])
        while queue:
            dis, r, c = heappop(queue)
            if r == destination[0] and c == destination[1]: return dis
            if visited.get((r,c), float('inf')) < dis: continue
            directions = ((1,0), (-1,0), (0,1), (0,-1))
            for i, j in directions:
                d = 0
                ir, ic = r,c
                while 0 <= ir + i < m and 0 <= ic + j < n and maze[ir+i][ic+j] != 1:
                    d += 1
                    ir += i
                    ic += j
                if visited.get((ir,ic), float('inf')) > dis + d:
                    heappush(queue, (dis+d, ir, ic))
                    visited[(ir,ic)] = dis+d
        return -1

print(Solution().shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
[0,4],
[3,2]))
        
