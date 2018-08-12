from collections import Counter
from heapq import heapify, heappop, heappush
class Solution:
    def rearrangeString(self, s, k):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c, ans = Counter(s), []
        heap = [(-value, key) for key, value in c.items()]
        heapify(heap)
        while heap:
            i, temp = 0, []
            while i < k:
                if heap:
                    count, ch = heappop(heap)
                    if -(count + 1) > 0:
                        temp.append((count+1, ch))
                    ans.append(ch)
                if not heap and not temp:
                    break
                i += 1
                if len(heap) < k-i:
                    if any(True if -count > 1 else False  for count, el in heap) or (not heap and temp):
                        return ""
            heap += temp
            heapify(heap)

        return ''.join(ans)
        
print(Solution().rearrangeString("aaadbbcc", 2))
