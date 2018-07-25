"""
https://leetcode.com/problems/cheapest-flights-within-k-stops
"""
from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        if not flights or src < 0 or src > n-1 or dst < 0 or dst > n-1 or K < 0:
            return -1
        if n < -1 : return -1
        graph = defaultdict(list)
        best = {}
        for u,v,w in flights:
            graph[u].append((v,w))
        pq = [(0,-1,src)]
        while pq:
            cost,k,node = heapq.heappop(pq)
            if k > K or cost > best.get((k,node), float('inf')): continue
            if node == dst: return cost
            for v,w in graph[node]:
                newcost  = w + cost
                if best.get((k+1, v), float('inf')) > newcost:
                    heapq.heappush(pq, (w+cost, k+1, v))
                    best[(k+1, v)] = newcost
        return -1

print(Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]],0,2,5))

