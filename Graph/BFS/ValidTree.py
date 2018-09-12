from collections import defaultdict, deque
from enum import Enum

class Color(Enum):
    WHITE = 0,
    GREY = 1,
    BLACK = 2

class Solution:
    def bfs(self, i , graph, visited):
        queue = deque([i])
        visited[i] = Color.GREY
        parent = {i : None}
        while queue:
            u = queue.popleft()
            visited[i] = Color.BLACK
            for v in graph[u]:
                if visited[v] != Color.WHITE and parent[u] != v:
                    return False
                elif visited[v] == Color.WHITE:
                    queue.append(v)
                    visited[v] = Color.GREY
                    parent[v] = u
        return True
                    

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [Color.WHITE] * n
        return all([self.bfs(i,graph, visited) for i in range(n) if visited[i] == Color.WHITE])

print(Solution().validTree(5, [[0,1], [0,2], [0,3], [1,4]]))
