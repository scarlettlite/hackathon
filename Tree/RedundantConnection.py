from collections import defaultdict
from enum import Enum
class Color(Enum):
    WHITE = 0,
    GREY = 1,
    BLACK = 2

class Solution:
    def dfs(self, u, visited, edges, graph, parent):
        if visited[u] == Color.WHITE:
            visited[u] = Color.GREY
            for v in graph[u]:
                if parent != v:
                    edges.append(list(sorted([u,v])))
                    if self.dfs(v, visited, edges, graph, u) == True:
                        return True
                    edges.pop()
            visited[u] = Color.BLACK
        elif visited[u] == Color.GREY:
            return True
        return False


    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        n = 1
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            if n < u:
                n = u
            if n < v:
                n = v

        visited = [Color.WHITE for _ in range(n+1)]
        cycle = []
        ans = []
        self.dfs(1, visited, cycle, graph, None)
        i = -1
        for c in cycle:
            i = max(edges.index(c), i)
        return edges[i]

print(Solution().findRedundantConnection([[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]))
            




        
