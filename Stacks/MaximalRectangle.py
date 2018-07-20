class Solution:
    def biggestRectangle(self, arr):
        stack = [-1]
        mv = 0
        for i,x in enumerate(arr):
            while stack and arr[stack[-1]] >= x:
                area = arr[stack.pop()] * (i-stack[-1]-1)
                mv = max(area,mv)
            else:
                stack.append(i)
        while stack:
            area = arr[stack.pop()] * (len(arr)-stack[-1]-1)
            mv = max(area,mv)
        return mv

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m = len(m)
        n = len(matrix[0])
        hist = [0 for _ in len(n)]
        maxrect = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    hist[j] += 1
                else:
                    hist[j] = 0
            maxrect = max(maxrect, self.biggestRectangle(hist))
        return maxrect

            