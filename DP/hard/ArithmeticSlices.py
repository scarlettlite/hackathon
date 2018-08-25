from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0
        seqs = [{}]
        weak = [{}]
        count = 0
        for i in range(1, len(A)):
            nd = {}
            for j in range(i):
                y = A[i] - A[j]
                if y not in nd:
                    nd[y] = 0
                nd[y] += 1
            weak.append(nd)

        for i in range(1, len(A)):
            x = A[i]
            nd = {}
            for j, dd in enumerate(seqs):
                y = x - A[j]
                if y in dd:
                    if y not in nd:
                        nd[y] = 0
                    if y not in weak[j]:
                        nd[y] += dd[y] + 1
                    else:
                        nd[y] += dd[y]
                if y in weak[j]:
                    if y not in nd:
                        nd[y] = 0
                    nd[y] += weak[j][y]
                count += nd.get(y,0)
            seqs.append(nd)
        return count


print(Solution().numberOfArithmeticSlices([1,1,1,1]))  