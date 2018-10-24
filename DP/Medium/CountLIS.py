class Solution:
	def findNumberOfLIS(self, nums):
		n = len(nums)
		length = [1 for _ in nums]
		count = [1 for _ in nums]
		longest = 0
		for j, x in enumerate(nums):
			for i in range(n):
				if nums[i] < nums[j]:
					if length[i] + 1 > length[j]:
						length[j] = length[i] + 1
						count[j] = count[i]
					elif length[i] + 1 == length[j]:
						count[j] += count[i]
		longest = max(length)
		return sum([ c for i,c in enumerate(count) if longest == length[i] ])