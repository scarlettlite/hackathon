"""
https://leetcode.com/problems/sliding-window-maximum
"""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = deque([0])
        result = []
        n = len(nums)
        for i in range(1,k):
            x = nums[i]
            while queue and nums[queue[-1]] < x:
                queue.pop()
            else:
                queue.append(i)

        for i in range(k,n):
            x = nums[i]
            result.append(nums[queue[0]])
            if queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < x:
                queue.pop()
            else:
                queue.append(i)
        result.append(nums[queue[0]])

        return result

print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 1))
            



