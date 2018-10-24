# Knight probability in chess
from collections import defaultdict
class Solution(object):
    def knightProbability(self, N, K, r, c):
        dp = defaultdict(int)
        dp[(r,c)] = 1
        directions = [ [2,1], [2, -1], [1, 2], [1, -2], [-2, -1], [-2, 1], [-1, 2], [-1, -2] ]
        for _ in range(K):
            new_dp = defaultdict(int)
            for position, probability in dp.items():
                for  dr, dc in directions:
                    nr, nc = position[0] + dr, position[1] + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        new_dp[(nr,nc)] += probability / 8
            dp = new_dp

        return sum(dp.values())