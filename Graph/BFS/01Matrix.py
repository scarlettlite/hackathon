from collections import deque
class Solution:    
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        distance = dict()
        queue = deque()
        m, n = len(matrix), len(matrix[0])
        distance = [[float('inf') for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i,j))
                    distance[i][j] = 0
        directions = ((1, 0), (-1, 0), (0,1), (0, -1))
        while queue:
            r,c =  queue.popleft()
            for di, dj in directions:
                ir, ic = r + di, c + dj
                if 0 <= ir < m and 0 <= ic < n:
                    if distance[ir][ic] > distance[r][c] + 1:
                        queue.append((ir, ic))
                        distance[ir][ic] = distance[r][c] + 1
        return distance

print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))