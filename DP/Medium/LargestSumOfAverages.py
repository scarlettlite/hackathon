class Solution:
    def average(self, cumulative_sum, i, j):
        return (cumulative_sum[ j + 1 ] - cumulative_sum[ i ] ) / (j - i + 1)

    def largestSumOfAverages(self, A, K):
        cumulative_sum = [0]
        n = len(A)
        for x in A:
            cumulative_sum.append(cumulative_sum[-1] + x)
        prev_dp = [ self.average(cumulative_sum, 0, i) for i in range(n) ]
        for k in range(1,K):
	        dp = [ 0 for _ in range(n) ]
	        for i in range(k, n):
		        for j in range(k-1, i):
			        dp [i] = max(dp[i], prev_dp[j] + self.average(cumulative_sum, j + 1, i))
	        prev_dp = dp

        return prev_dp [-1] 
        
print(Solution().largestSumOfAverages([9,1,2,3,9], 3))