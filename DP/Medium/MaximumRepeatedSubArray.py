class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m = len(A)
        n = len(B)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        mx = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] =  1 + dp[i-1][j-1]
                    mx = max(mx, dp[i][j])
        return mx

print(Solution().findLength([1,2,3,2,1], [4,3,2,1,5]))
        