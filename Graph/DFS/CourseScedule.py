"""
https://leetcode.com/problems/course-schedule
"""
from collections import defaultdict
from enum import Enum
class color(Enum):
    WHITE = "white"
    GREY = "grey"
    BLACK = "black"

class Solution:
    def dfs(self, node, graph, visited):
        result = True
        if visited[node] == color.GREY:
            result = False
        if visited[node] == color.WHITE:
            visited[node] = color.GREY
            for n in graph[node]:
                result = result and self.dfs(n, graph, visited)
            visited[node] = color.BLACK
        return result


    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)

        for u,v in prerequisites:
            graph[u].append(v)

        visited = [color.WHITE for i in range(numCourses)]
        result = True
        for n in range(numCourses):
            result = result and self.dfs(n, graph, visited)
            if result == False: return result
        return result

print(Solution().canFinish(5, [[0,1], [1,2], [3,2], [4,1], [2,4]]))


