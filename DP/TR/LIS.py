"""
Find the Longest Subsequence in an array with
negative and positive numbers
"""
class Solution :
    def lis(self, arr):
        n = len(arr)
        dp = [1 for i in range(n)]
        ans = [-1 for i in range(n)]
        ml = 0
        mi = -1
        for i in range(1,n):
            for j in range(0,i):
                if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    ans[i] = j
                    if ml < dp[i]:
                        ml = dp[i]
                        mi = i
        l = []
        i = mi
        while i > 0:
            l.append(arr[i])
            i = ans[i]
        print(l[::-1])
        return ml


Solution().lis([3,4,-1,0,6,2,3])




        