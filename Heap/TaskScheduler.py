from heapq import heapify, heappop, heappush
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c, time = Counter(tasks), 0
        heap = [(-value, key) for key, value in c.items()]
        heapify(heap)
        while heap:
            k, temp = 0, []
            while k <= n:
                if heap:
                    count, task = heappop(heap)
                    if -(count + 1) > 0: 
                        temp.append((count + 1, task))
                time += 1
                if not heap and not temp: break
                k += 1
            heap += temp
            heapify(heap)
        return time

#print(Solution().leastInterval(["A","A","A","B","B","B"], 2))

"""
Approach : Empty Slots
"""

class Solution1:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c = Counter(tasks)
        el, count = c.most_common(1)[0]
        emptyslots = (count-1) * n
        del c[el]
        for x in c.values():
            emptyslots -= min(x, count-1)
    
        return len(tasks) + emptyslots

print(Solution1().leastInterval(["A","A","A","B","B","B"], 2))


                
