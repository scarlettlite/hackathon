from collections import deque, defaultdict 
class Solution:
    def __init__(self):
        self.directions = ((1,0),(0,1),(-1,0),(0,-1))

    def ispacificreachable(self, r, c, matrix):
        if r == 0 or c == 0:
            return True
        return False

    def isatlanticreachable(self, r, c, matrix):
        m, n = len(matrix), len(matrix[0])
        if r == m-1 or c == n-1:
            return True

    def isoceanreachable(self, r, c, matrix, oceandict, func):
        m, n = len(matrix), len(matrix[0])
        if func(r,c,matrix) == True:
            return True
        for di, dj in self.directions:
            ir, ic = r + di, c + dj
            if 0 <= ir < m and 0 <= ic < n and oceandict[(ir,ic)] == True:
                return True
        return False

    def bfs(self, queue, matrix, oceandict, isoceanreachable):
        m, n = len(matrix), len(matrix[0])
        while queue:
            r, c= queue.popleft()
            if oceandict[(r,c)] == True:
                continue
            if self.isoceanreachable(r,c,matrix,oceandict,isoceanreachable):
                oceandict[(r,c)] = True
            for di, dj in self.directions:
                ir, ic =  r + di, c + dj
                if 0 <= ir < m and 0 <= ic < n and matrix[ir][ic] >= matrix[r][c]:
                    if not oceandict[(ir,ic)] :
                        queue.append((ir,ic))

        
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]: return []
        queue = deque([])
        m, n = len(matrix), len(matrix[0])
        pacific, atlantic = defaultdict(bool),defaultdict(bool)
        for j in range(n): queue.append((0,j))
        for i in range(m): queue.append((i,0))
        self.bfs(queue, matrix, pacific, self.ispacificreachable)

        for j in range(n): queue.append((m-1,j))
        for i in range(m): queue.append((i,n-1))

        self.bfs(queue, matrix, atlantic, self.isatlanticreachable)
        
        ans = []
        for key in pacific.keys():
            if pacific[key] == True and atlantic[key] == True:
                ans.append(key)
        return ans

print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
                
