

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        key = 23
        def guess(x):
            if x == key:
                return 0
            elif x > key:
                return -1
            else:
                return 1 


        lo, hi = 1, n
        while lo < hi:
            mid = (lo+hi)//2
            if guess(mid) == -1:
                hi = mid - 1
            elif guess(mid) == 1:
                lo = mid + 1
            else:
                break
        return lo

print(Solution().guessNumber(67))