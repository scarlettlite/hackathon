class Solution:
    def atMostNGivenDigitSet(self, D, N):
        s = str(N)
        k = len(s)
        lenD = len(d)
        dp = [0] * k + [1]
        for i in range(k-1, -1, -1):
            for d in D:
                if d < s[i]:
                    dp[i] +=  pow(lenD, k - i - 1)
                elif d == s[i]:
                    dp[i] += dp[i+1]

        return dp[0] + sum(pow(lenD, i) for i in range(1, k))
        
print(Solution().atMostNGivenDigitSet(["1","3","5","7"], 2435))