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
        res = ""
        i = 0
        heap = [[value,key] for key, value in c.items()]
        heap.sort(key=lambda x: x[1], reverse=True)
        while i < len(S):
            for x in heap:
                if x[0] > 0 :
                   res += x[1]
                   x[0] -= 1 
                   i += 1
        return res

print(Solution().reorganizeString("abb"))

            
        

