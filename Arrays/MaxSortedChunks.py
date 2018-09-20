class Solution(object):
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i: 
                ans += 1
        return ans

print(Solution().maxChunksToSorted([0,2,3,1,6,4,5]))