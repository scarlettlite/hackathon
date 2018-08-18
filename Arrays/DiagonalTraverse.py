class Solution:
    def parse(self, matrix, r,c):
        stack = []
        m, n = len(matrix), len(matrix[0])
        while 0 <= r < m and 0 <= c < n:
            stack.append(matrix[r][c])
            r += 1
            c -= 1
        return stack
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        ans = []
        stack =  []
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            r, c = 0, j
            if j & 1 == 0:
                ans.extend(self.parse(matrix,r,c)[::-1])
                stack.clear()
            else:
                ans.extend(self.parse(matrix,r,c)[:])
                stack.clear()
        
        for i in range(1, m):
            r, c = i, n-1
            if (i & 1 == 1 and n & 1 == 0) or (i & 1 == 0 and n & 1 == 1):
                ans.extend(self.parse(matrix,r,c)[::-1])
                stack.clear()
            else:
                ans.extend(self.parse(matrix,r,c)[:])
                stack.clear()
        return ans

print(Solution().findDiagonalOrder([
 [ 1, 2, 3],
 [ 4, 5, 6],
 [ 7, 8, 9]
]))

print(Solution().findDiagonalOrder([
 [ 1, 2, 3, 4],
 [ 4, 5, 6, 5],
 [ 7, 8, 9, 6]
]))

#[1,2,4,7,5,3,6,8,9]