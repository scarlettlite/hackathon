class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = 1.0
        if n < 0:
            x = 1/x
            n = -n
        i = n
        while i > 0:
            if i % 2 == 1:
                ans *= x
            x *= x
            i //=2

        return ans

print(Solution().myPow(2,10))