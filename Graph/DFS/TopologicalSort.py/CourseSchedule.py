from collections import defaultdict
from enum import Enum

class Color(Enum):
    WHITE = "white"
    GREY = "grey"
    BLACK = "black"

class Solution:
    def dfs(self, node, graph, visited, ordering):
        result = True
        if visited[node] == Color.GREY:
            result = False
        if visited[node] == Color.WHITE:
            visited[node] = Color.GREY
            for v in graph[node]:
                result = result and self.dfs(v, graph, visited, ordering)
                if result == False: return result
            visited[node] = Color.BLACK
            ordering.append(node)
        return result

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)
        visited = [Color.WHITE for i in range(numCourses)]
        result = True
        ordering = []
        for i in range(numCourses):
            result = result and self.dfs(i, graph, visited, ordering)
            if result == False: return []
        return ordering[::-1]

print(Solution().findOrder(4, [[1,0],[2,0],[1,3],[0,2]]))
