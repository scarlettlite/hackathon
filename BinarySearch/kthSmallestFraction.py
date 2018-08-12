from fractions import Fraction
class Solution(object):
    def kthSmallestPrimeFraction(self, primes, K):
        def under(x):
            left, best = 0, 0
            for j in range(1, len(primes)):
                while primes[left] < primes[j] * x:
                    left += 1
                count += left
                if left > 0:
                    best = max(best, Fraction(primes[left-1], primes[j]))
            return count, best
        
        lo, hi, mid =  0.0, 1.0, 0.0
        while hi-lo > 1e-9:
            mid = (lo + hi)/2.0
            count, best = under(mid)
            if count < K:
                lo = mid
            else:
                ans = best
                hi = mid
        return ans.numerator, ans.denominator

print(Solution().kthSmallestPrimeFraction([1,2,3,5], 3))