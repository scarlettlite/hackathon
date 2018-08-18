"""
Given a set of weighted jobs with start and stop times calculate 
the maximum profit you can obtain by scheduling these jobs
 the jobs must not overlap with each other
"""

class Solution:
    def wjs(self, arr, costs):
        """
        Sort the jobs according to end times in an non-decreasing order
        """
        arr.sort(key=lambda x:x[1])
        n = len(costs)
        dp = [costs[i] for i in range(n)]
        sol = [-1 for i in range(n)]
        mv = 0
        mi = -1
        for i in range(1, n):
            for j in range(0,i):
                if arr[i][0] > arr[j][1]:
                    if dp[i] < dp[j] + costs[i]:
                        dp[i] = dp[j] + costs[i]
                        sol[i] = j
                        if mv < dp[i]:
                            mv = max(mv, dp[i])
                            mi = i

        self.printSol(mi, sol, arr)
        return mv
        
    def printSol(self, mi, sol, arr):
        i = mi
        ans = []
        while i > -1:
            ans.append(arr[i])
            i = sol[i]
        print ans[::-1]

Solution().wjs([[6,7], [5,8], [7,9], [1,3], [2,5], [4,6]], [5,6,5,4,11,2])

        