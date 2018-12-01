
#Out of Boundary Paths
from collections import defaultdict
class Solution:
    def findPaths(self, m, n, N, i, j):
        dp = defaultdict(lambda: 0)
        dp[(i,j)] = 1
        M = pow(10, 9) + 7
        count = 0
        directions = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
        for k in range(N):
            new_dp = defaultdict(lambda: 0)
            for position, num_of_paths  in  dp.items():
                for dr, dc in directions:
                    r, c = position[0] + dr, position[1] + dc
                    if 0 <= r < m and 0 <= c < n:
                        if r == m-1 or c == n-1 or r == 0 or c == 0:
                            count = (count + dp[position]) % M
                        dp[(r,c)] = (dp[(r,c)] + dp[position]) % M	
            dp = new_dp
        return count