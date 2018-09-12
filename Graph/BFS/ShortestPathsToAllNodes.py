from collections import defaultdict, deque
class Solution:
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        distance = defaultdict(lambda:n*n)
        queue = deque([(1<<i, i) for i in range(n)])
        for i in range(n): distance[(1 << i, i)]:0 
        finalstate = pow(2,n) - 1
        while queue:
            state, parent = queue.popleft()
            d = distance[(state, parent)]
            if finalstate == state:
                return d
            for child in graph[parent]:
                newstate = 1 << child | state
                if distance[(newstate, child)] > d + 1:
                    distance[(newstate, child)] = d + 1
                    queue.append((newstate, child))
        


