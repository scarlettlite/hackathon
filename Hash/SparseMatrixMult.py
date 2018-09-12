from collections import defaultdict

class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        l,m,n = len(A), len(A[0]), len(B[0])
        C = [[0]*n for i in range(l)]
        da = defaultdict(list)
        for i in range(l):
            for j in range(m):
                if A[i][j] != 0:
                    da[i].append((j, A[i][j]))
        db = defaultdict(list)
        for j in range(m):
            for k in range(n):
                if B[j][k] != 0:
                    db[k].append((j, B[i][j]))
        
        for i in range(l):
            for k in range(n):
                if i in da and k in db:
                    for x in da[i]:
                        for y in db[k]:
                            if x[0] == y[0]:
                                C[i][k] += x[1]*y[1]

        return C

print(Solution().multiply([[1,0,0],[-1,0,3]],
[[7,0,0],[0,0,0],[0,0,1]]))