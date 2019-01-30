class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        inf = float("inf")
        n = len(words)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = maxWidth - len(words[i])
            for j in range(i+1,n):
                dp[i][j] = dp[i][j-1] - len(words[j]) - 1

        for i in range(n):
            for j in range(i,n):
                if dp[i][j] < 0:
                    dp[i][j] = inf
                else:
                    dp[i][j] = pow(dp[i][j],2)

        minCost = [dp[i][n-1] for i in range(n)]
        result = [n]*n
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if dp[i][j-1] == inf:
                    continue
                else:
                    if minCost[i] > minCost[j] + dp[i][j-1]:
                        minCost[i] = minCost[j] + dp[i][j-1]
                        result[i] = j
        justifiedText = []
        i = 0
        while i < n:
            justifiedText.append(" ".join(words[i:result[i]]))
            i = result[i]
        print(justifiedText)

print(Solution().fullJustify(["Tushar","roy","likes","to", "code"], 10))