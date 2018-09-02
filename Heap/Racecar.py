from math import log2, ceil
from heapq import heappop, heappush
class Solution(object):
    def racecar(self, target):
        barrier = pow(2, ceil(log2(target))) - 1
        pq = [(0, 0, 1)]#steps, pos, speed
        distance = {}
        s = 0
        while pq:
            steps, pos, speed = heappop(pq)
            s+=1
            if distance.get((pos,speed), float('inf')) < steps:
                continue
            if pos == target:
                return steps
            distance[pos,speed] = steps
            #accelerate
            if 0 <= pos + speed <= barrier and distance.get((pos + speed,2*speed), float('inf')) > steps + 1:
                heappush(pq, (steps+1, pos + speed, 2*speed))
                #reverse
            if speed > 0:
                if distance.get((pos, -1), float('inf')) > steps + 1:
                    heappush(pq, (steps+1, pos, -1))
            else:
                if distance.get((pos, 1), float('inf')) > steps + 1:
                    heappush(pq, (steps+1, pos, 1))

print(Solution().racecar(100))

                
        
