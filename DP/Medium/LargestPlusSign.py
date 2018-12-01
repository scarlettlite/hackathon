class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        banned = { tuple(mine) for mine in mines }
        m, n = N,N
        dp = [ [ 0 for _ in range(n) ]  for _ in range(m) ]
        ans  = 0
        for r in range(m):
            count = 0
            for c in range(n):
                count = 0 if (r,c) not in banned else count + 1
                dp[r][c] = count

        count = 0
        for c in range(n-1, -1, -1):
            count = 0 if(r,c) not in banned else count + 1
            dp[r][c] = min(count, dp[r][c] )	

        for c in range(n):
            count = 0
            for r in range(m):
                count = 0 if (r,c) not in banned else count + 1
                dp[r][c] = min(dp[r][c], count)
        count = 0
        for r in range(m-1,-1,-1):
            count = 0 if (r,c) not in banned else count + 1
            dp[r][c] = min(dp[r][c], count)
            ans = max(ans, dp[r][c])
        return ans