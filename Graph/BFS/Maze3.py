from heapq import heappop, heappush
class Solution:
    def getnext(self, maze, start, stop):
        directions = ((1, 0, 'd'), (-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l'))
        rv = []
        m,n = len(maze), len(maze[0])
        for i, j, direction in directions:
            r,c = start
            distance = 0
            while (0 <= r + i < m and 0 <= c + j < n and maze[r+i][c+j] != 1):
                r += i
                c += j
                distance += 1
                if r == stop[0] and c == stop[1]:
                    break
            if distance > 0:
                rv.append((r,c,distance, direction))
        return rv
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        pq = [(0, '', ball[0], ball[1])]
        visited = {}
        while pq:
            distance, direction, r, c = heappop(pq)
            if r == hole[0] and c == hole[1]:
                return direction
            if visited.get((r,c), (float('inf'), 'z')) < (distance, direction):
                continue
            nexts = self.getnext(maze, (r,c), hole)
            for i, j, disn, dirn in nexts:
                newcost = (distance + disn, direction + dirn)
                if visited.get((i,j), (float('inf'), 'z')) > newcost:
                    visited[(i,j)] = newcost
                    heappush(pq, (newcost + (i,j)))
        return 'impossible'

print(Solution().findShortestWay([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]],
[4,3],
[3,0]))

            
        