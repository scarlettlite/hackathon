from heapq import heappop, heappush
class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        current = []
        future = []
        for c, p in zip(Capital, Profits):
            heappush(future, (c,p))
        for _ in range(k):
            while future and future[0][0] <= W:
                heappush(current, -heappop(future)[1])
            if current:
                W -= heappop(current)

        return W

print(Solution().findMaximizedCapital(2, 2, [2,3,5,1,7,3], [1,2,3,5,6,7]))


