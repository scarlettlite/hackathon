class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        if not matrix or not matrix[0]: return ans
        m, n = len(matrix), len(matrix[0])
        rb, re = 0, m-1
        cb, ce = 0, n-1
        t = m*n
        while len(ans) < t:
            if len(ans) < t:
                for i in range(cb, ce+1):
                    ans.append(matrix[rb][i])
            rb += 1
            if len(ans) < t:
                for i in range(rb , re+1):
                    ans.append(matrix[i][ce])
            ce -= 1
            if len(ans) < t:
                for i in range(ce, cb-1, -1):
                    ans.append(matrix[re][i])
            re -= 1
            if len(ans) < t:
                for i in range(re, rb-1, -1):
                    ans.append(matrix[i][cb])
            cb += 1

        return ans

# print(Solution().spiralOrder([
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]))

print(Solution().spiralOrder([
  [1, 2, 3, 4, 5],
  [5, 6, 7, 8, 25],
  [9,10,11,12, 625],
  [3, 9,27,81, 243]
]))