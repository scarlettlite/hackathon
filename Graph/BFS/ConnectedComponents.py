from collections import defaultdict, deque
from enum import Enum
class Color(Enum):
    WHITE = 0,
    GREY = 1,
    BLACK = 2

class Solution:
    def bfs(self, node, graph, visited):
        queue = deque([node])
        visited[node] = Color.GREY
        while queue:
            u = queue.popleft()
            visited[node] = Color.BLACK
            for v in graph[u]:
                if visited[v] == Color.WHITE:
                    queue.append(v)
                    visited[v] = Color.GREY
        

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [Color.WHITE for _ in range(n)]
        components = 0
        for i in range(n):
            if visited[i] == Color.WHITE:
                self.bfs(i, graph, visited)
                components += 1
        return components

print(Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]))

