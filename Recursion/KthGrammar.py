class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return 0
        parent = self.kthGrammar(N-1, (K+1) // 2)
        p = (K+1) // 2
        value = None
        if parent == 0:
            if 2*(p) - 1 == K:
                value = 0
            else:
                value = 1
        else:
            if 2*(p) - 1 == K:
                value = 1
            else:
                value = 0
                
        return value

print(Solution().kthGrammar(4,5))