#2143195649

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        ans = 0
        while True:
            middle = (low + high)/2
            k = pow(middle, 2)
            k2 = pow(middle+1, 2)
            if k <= x <= k2:
                ans = middle
                if k2 == x:
                    ans = middle + 1
                break
            elif k < x:
                low = middle
            elif k > x:
                high = middle
        #print(i)
        return ans

print(Solution().mySqrt(1579205274))
                        