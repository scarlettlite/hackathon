
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0
        nums = [1 if i > 1 else 0 for i in range(n)]
        ans = 0
        p = 2
        while p < pow(n, 0.5):
            if nums[p] != 0:
                for i in range(p*p,n,p):
                    nums[i] = 0
            p += 1
        return sum(nums)

print(Solution().countPrimes(20))