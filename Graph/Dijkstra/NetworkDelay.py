"""
https://leetcode.com/problems/network-delay-time
"""
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times, N,K):
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        pq = [(0,K)]
        dist = defaultdict(int)
        while pq:
            d, node = heapq.heappop(pq)
            """
            works like a heap decrease priority operation
            """
            if node in dist: 
                continue
            dist[node] = d
            for neighbor, weight in graph[node]:
                if dist.get(neighbor) == None:
                    heapq.heappush(pq, (d + weight, neighbor))
        return max(dist.values()) if len(dist)  == N else -1

print(Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,2]],
3,
1))

