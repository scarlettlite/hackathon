from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        c = Counter(S)
        N = len(S)
        if c.most_common(1)[0][1] > (N+1)//2:
            return ""
        res = []
        heap = [(-value, key) for key, value in c.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            nc1, ch1 = heapq.heappop(heap)
            nc2, ch2 = heapq.heappop(heap)
            res.extend([ch1, ch2])
            if -(nc1 + 1) > 0: heapq.heappush(heap, (nc1+1, ch1))
            if -(nc2 + 1) > 0: heapq.heappush(heap, (nc2+1, ch2))
        else:
            nc1, ch1 = heapq.heappop(heap)
            res.append(ch1)
        return ''.join(res)

print(Solution().reorganizeString("aaabbbbcderty"))

            
        

