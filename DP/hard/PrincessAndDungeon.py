class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        
        R, C = len(dungeon), len(dungeon[0])
        dp = [[0] * C for _ in range(R)]
        dp[-1][-1] = max(1 - dungeon[-1][-1], 1)
        for i in range(R - 2, -1, -1):
            dp[i][C - 1] = max(dp[i + 1][C - 1] - dungeon[i][C - 1], 1)
        for i in range(C - 2, -1, -1):
            dp[R - 1][i] = max(dp[R - 1][i + 1] - dungeon[R - 1][i], 1)
        
        for i in range(R - 2, -1, -1):
            for j in range(C - 2, -1, -1):
                # if adding health is much larger than health required, set it to 1
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        
        return dp[0][0]

    def calculateMinimumHPRecursive(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m,n = len(dungeon),len(dungeon[0])
        d={(m-1,n-1):max(1,1-dungeon[m-1][n-1])}
        def helper(i,j):
            if (i,j) in d: return d[i,j]
            if i==m-1:
                d[i,j]=max(1,helper(i,j+1)-dungeon[i][j])
            elif j==n-1:
                d[i,j]=max(1,helper(i+1,j)-dungeon[i][j])
            else:
                d[i,j] = max(1,min(helper(i+1,j),helper(i,j+1))-dungeon[i][j])
            return d[i,j]
        return helper(0,0)


print(Solution().calculateMinimumHPRecursive([[-2,-3,3],[-5,-10,1],[10,30,-5]]))


               