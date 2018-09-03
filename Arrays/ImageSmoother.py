class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(M), len(M[0])
        ans = [[0 for j in range(n)] for i in range(m)]
        directions = ((1,1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1),(1,-1),(-1,1))
        for i in range(m):
            for j in range(n):
                s = M[i][j]
                n = 1
                for di, dj in directions:
                    ir, ic = i + di, j + dj
                    if 0 <= ir < m and 0 <= ic < n:
                        s += M[ir][ic]
                        n += 1
                ans[i][j] = int(s/n)
        return ans
                        
