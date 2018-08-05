from collections import defaultdict
from enum import Enum
class Color(Enum):
    WHITE = 0,
    GREY = 1,
    BLACK = 2

class Solution:
    def dfs(self, u, visited, edges, graph):
        if visited[u] == Color.WHITE:
            visited[u] = Color.GREY
            for v in graph[u]:
                edges.append([u,v])
                if self.dfs(v, visited, edges, graph) == True:
                    return True
                edges.pop()
            visited[u] = Color.BLACK
        else:
            return True


    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        n = 1
        for u,v in edges:
            graph[u].append(v)
            if n < u:
                n = u
            if n < v:
                n = v

        visited = [Color.WHITE for _ in range(n+1)]
        cycle = []
        ans = []
        self.dfs(1, visited, cycle, graph)
        return cycle[-1]

print(Solution().findRedundantDirectedConnection([[1,2], [1,3], [2,3]]))