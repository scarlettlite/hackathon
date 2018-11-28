class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        csum = []
        n = len(nums)
        ss = 0
        for i, x in enumerate(n):
            ss += x
            if i >= k: 
                ss -= nums[i-k]
            if i >= k-1:
                csum.append(ss)
        l = len(csum)
        left = [0]*l
        right = [0]*l
        best = 0
        for i in range(l):
            if csum[i] > csum[best]:
                best = i
            left[i] = best
        best = l-1
        for i in range(l-1, -1, -1):
            if csum[i] > csum[best]:
                best = i
            right[i] = best

        ans = None
        for j in range(k, l - k):
            i, k = left[j - k], right[j + k]
            if ans == None or csum[i] + csum[j] + csum[k] >= csum[ans[0]] + csum[ans[1]] + csum[ans[2]]:
                ans = i,j,k
        return ans

            

            