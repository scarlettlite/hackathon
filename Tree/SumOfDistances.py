from collections import defaultdict
from enum import Enum
class Color:
    WHITE = 0,
    GREY = 1,
    BLACK = 2

class Solution:
    def creategraph(self, edges):
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
        return graph

    def dfs(self, u, visited, graph, stack, dis):
        if visited[u] == Color.WHITE:
            visited[u] = Color.GREY
            stack.append(u)
            for v in graph[u]:
                for i, p in enumerate(stack):
                    dis[v][p] = dis[p][v] = len(stack) - i
                self.dfs(v, visited, graph, stack, dis)
            stack.pop()
            visited[u] = Color.BLACK

    def dfs2(self, dis, graph, p, u):
        for p in range(N):
            for u in graph[p]:
                for v in graph[p]:
                    if u != v:
                        d[u][v] = d[v][u] = dis[u][0] + dis[0][v]
            
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        visited = [Color.WHITE for _ in range(N)]
        dis = [[0 for _ in range(N)] for _ in range(N)]
        graph = self.creategraph(edges)
        self.dfs(0, visited, graph, [], dis)
        self.dfs2(dis)

        return sum([sum(row) for row in dis])

print(Solution().sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))

