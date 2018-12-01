class Solution:
    def minimumDeleteSum(self, word1, word2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [0] * (n+1)
        for i in range(m+1):
            new_dp = [0] * (n+1)
            for j in range(n+1):
                if i==0 and j == 0:
                    continue
                if i == 0 and j != 0:
                    new_dp[j] = new_dp[j-1] + ord(word2[j-1])
                elif j == 0 and i != 0:
                    new_dp[j] = dp[j] + ord(word1[i-1])
                elif word1[i-1] == word2[j-1]:
                    new_dp[j] = dp[j-1]
                else:
                    new_dp[j] = min(dp[j-1] + ord(word1[i-1]), new_dp[j-1] + ord(word2[j-1]))
            print(dp, new_dp)
            dp = new_dp
                
        return dp[-1]

print(Solution().minimumDeleteSum("sea", "eat"))