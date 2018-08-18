from collections import defaultdict
class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        index = {x:i for i,x in enumerate(A)}
        dd = defaultdict(lambda : 2)
        mv = 0
        for i,x in enumerate(A):
            for j in range(i):
                k = index.get(x-A[j], None)
                if k is not None and k < j:
                    c = dd[j,i] = dd[k,j] + 1
                    mv = max(mv, c)
        return mv if mv > 2 else 0
                    
print(Solution().lenLongestFibSubseq([2,4,7,8,9,10,14,15,18,23,32,50]))