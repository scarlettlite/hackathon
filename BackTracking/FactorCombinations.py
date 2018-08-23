import math 
class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        sq = int(pow(n, 0.5)) + 1
        return self.helper(n, 2, sq, [])

    def helper(self, n, start, sq, tmp):
        ans = []
        for i in range(start, sq):
            q, r = divmod(n, i)
            if r == 0 and q >= i:
               tmp.append(i)
               ans.append(tmp + [q])
               """
               Like coin change Allow user to repeat a factor
               """
               ans.extend(self.helper(q, i, sq, tmp))
               tmp.pop()
        return ans




print(Solution().getFactors(12))