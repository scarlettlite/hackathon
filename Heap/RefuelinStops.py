from collections import deque
class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        stations = [(0, startFuel)] + stations + [[target,0]]
        heap, n = deque([(0, 0, 0)]), len(stations)
        distance = {}
        while heap:
            d, remfuel, idx = heap.popleft()
            pos, fuel = stations[idx]
            fuel += remfuel
            # if pos in distance and distance[pos] < d:
            #     continue
            if pos >= target:
                return d-1
            distance[pos] = d
            i = idx + 1
            while i < n:
                nextpos = stations[i][0]
                if pos + fuel >= nextpos:
                    heap.append((d+1, pos + fuel - (nextpos),i))
                    i += 1
                else:
                    break
        return -1

print(Solution().minRefuelStops(1000,
299,
[[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]))
