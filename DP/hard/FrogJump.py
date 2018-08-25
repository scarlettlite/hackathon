from heapq import heappush, heappop
class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        heap = [(1,1)]
        last = stones[-1]
        stones = set(stones[2:])
        visited = set()
        while heap:
            s, k = heappop(heap)
            if s == last:
                return True
            for i in range(k-1, k+2):
                n = i + s
                if n in stones and i > 0 and (n, i) not in visited:
                    visited.add((n, i))
                    heappush(heap, (n, i))
        return False

print(Solution().canCross([0,1,2,3,4,8,9,11]))