class Solution:
    def __init__(self):
        self.ans = []

    def helper(self, k, n, added, beg, end):
        if k == 0 and n == 0:
            self.ans.append(added[:])
        elif n > 0 and k > 0:
            for x in range(beg, end):
                if x <= n:
                    added.append(x)
                    self.helper(k-1, n-x, added, x+1, end)
                    added.pop()

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        end = 10 if n >= 9 else n-k+1
        self.helper(k,n,[], 1, end)
        return self.ans

print(Solution().combinationSum3(2,9))