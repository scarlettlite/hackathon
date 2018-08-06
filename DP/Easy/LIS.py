from bisect import bisect_right
from collections import deque
class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs: return 0
        pairs.sort(key=lambda x: x[0])
        keys = deque([pairs[0][1]])
        p = deque([pairs[0]])
        n = len(pairs)
        for i in range(1,n):
            index = bisect_right(keys, pairs[i][0])
            if ( 0 < index < len(keys) and p[index-1][1] < pairs[i][0] and p[index][0] > pairs[i][1]) or(index == 0 and pairs[i][1] < p[0][0]) or (index == len(keys) and pairs[i][0] > p[-1][1]):
                keys.insert(index, pairs[i][1])
                p.insert(index, pairs[i])
        return len(keys)

print(Solution().findLongestChain([[0,1],[2,3],[3,5],[4,6],[-3,-1],[8,10],[1,3], [5,6], [-5,-1]]))



"""
optimal solution
def findLongestChain(self, pairs):
    cur, ans = float('-inf'), 0
    for x, y in sorted(pairs, key = operator.itemgetter(1)):
        if cur < x:
            cur = y
            ans += 1
    return ans
"""