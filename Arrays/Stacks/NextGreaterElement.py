"""
https://leetcode.com/problems/next-greater-element-ii/description/
"""
class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums : return nums
        n = len(nums)
        result = [-1 for _ in range(n)]
        stack = []
        for i in range(n):
            if not stack:
                stack.append(i)
            else:
                while stack and nums[stack[-1]] < nums[i]:
                    index = stack.pop()
                    result[index] = nums[i]
                else:
                    stack.append(i)
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                result[index] = nums[i]
        return result

print(Solution().nextGreaterElements([1,2,3,2,1]))