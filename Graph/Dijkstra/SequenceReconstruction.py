"""
https://leetcode.com/problems/sequence-reconstruction
"""
from collections import defaultdict
import heapq

class Solution:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if not org or not seqs: return False
        graph = defaultdict(list)
        pathdict = defaultdict(int)
        distance = defaultdict(int)

        for seq in seqs:
            for i in range(1, len(seq)):
                if (seq[i], 1) not in graph[seq[i-1]]:
                    graph[seq[i-1]].append((seq[i], 1))

        start = org[0]
        stop = org[-1]
        pq = [(0, start, -1)]
        parent = -1
        while pq:
            d, node, p = heapq.heappop(pq)
            if node in distance: continue
            distance[node] = d
            pathdict[node] = p
            for v,w in graph[node]:
                if v not in distance:
                    heapq.heappush(pq, (d+w, v, node))
        path = []
        s = stop
        while s != -1:
            path.append(s)
            s = pathdict[s]
        path.reverse()
        if len(path) != len(org):
            return False
        else:
            return all([True if i==j else False for i,j in zip(org, path)])

print(Solution().sequenceReconstruction([1,2,3], [[5,2,6,3],[4,1,5,2]]))

