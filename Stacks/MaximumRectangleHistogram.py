class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights: return 0
        ans = 0
        n = len(heights)
        """
        taking -1 is critical here, it helps you write less code
        """
        stack = [-1]
        for i,x in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= x:
                j = stack.pop()
                """
                value at index j is the minimum value seen in the range
                [stack.top()+1 , j-1]
                """
                ans = max(ans, heights[j] * (i-stack[-1]-1))
            else:
                stack.append(i)
        while stack[-1] != -1:
            j = stack.pop()
            """
                value at index j is the minimum value seen in the range
                [stack.top()+1 , n-1]
            """
            ans = max(ans, heights[j] * (n-stack[-1]-1))

        return ans

Solution().largestRectangleArea([2,1,5,6,2,3])
