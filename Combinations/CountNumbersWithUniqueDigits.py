"""
https://leetcode.com/problems/count-numbers-with-unique-digits
"""

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        result = 10
        cum = 9
        c = 9
        for i in range(2,n+1):
            cum = cum * c
            result += (cum)
            c -= 1
        return result
    

print(Solution().countNumbersWithUniqueDigits(1))
        