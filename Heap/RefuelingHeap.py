from heapq import heappop, heappush
class Solution(object):
    def minRefuelStops(self, target, tank, stations):
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, float('inf')))

        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:  # must refuel in past
                tank += -heappop(pq)
                ans += 1
            if tank < 0: return -1
            heappush(pq, -capacity)
            prev = location

        return ans
print(Solution().minRefuelStops(1000,
299,
[[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]))