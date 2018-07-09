class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights: return 0
        ans = 0
        stack = []
        for i,x in enumerate(heights):
            if not stack:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] >= x:
                    j = stack.pop()
                    ans = max(ans, x * i-j)
                else:
                    stack.apped(stack)
        while stack:
            index = sta

