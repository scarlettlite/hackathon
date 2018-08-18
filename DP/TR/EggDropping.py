"""
What is the minimum number of attempts it takes to find out
from which floor the egg will break
"""
"""
if an egg does not break on a floor, then it will not break on the floors below it
if an egg breaks on a floor then it will break on all floors above it
"""

class Solution:
    def eggDroppingPuzzles(self, eggs, floors):
        if not eggs or not floors: return 0
        eggs = eggs + 1
        floors = floors + 1
        dp = [[0 if i == 0 or j == 0 else float("inf") for j in range(floors)] for i in range(eggs)]
        for i in range(1, floors):
            dp[1][i]=  dp[1][i-1] + 1 
        for i in range(2, eggs):
            for j in range(1, floors):
                for k in range(1,j+1):
                    """
                    on floor j and with eggs i, We drop an egg,
                    if it breaks we have one less egg and one less floor to
                    work with and if the egg doesnt break, then we have j-k floors 
                    to test with i eggs
                    """
                    dp[i][j] = min(dp[i][j], 1+ max(dp[i-1][k-1], dp[i][j-k]))

        return dp[-1][-1]

print(Solution().eggDroppingPuzzles(2,6))