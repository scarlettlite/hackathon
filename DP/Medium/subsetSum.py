"""
Whether an Array Contains a subset which adds up to given target
"""
class Solution:
    def subsetSum(self, arr, tot):
        if not arr and tot == 0: return True
        n = len(arr)+1
        m = tot+1
        arr = [0]+arr
        dp = [[True if i == 0 else False for j in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1]
                if i >= arr[j]:
                    if dp[i-arr[j]][j-1]:
                        dp[i][j] = dp[i][j-1] or dp[i-arr[j]][j-1]
            
        print(self.printSol(dp, arr))
        return dp[-1][-1]

    def printSol(self, dp, arr):
        m = len(dp) - 1
        n = len(dp[0]) - 1
        ans = []
        while m>0:
            while n >= 0 and dp[m][n-1] == True:
                n = n-1
            ans.append(arr[n])
            m = m - arr[n]
        return ans
    
print(Solution().subsetSum([2,3,7,8,10] ,19))