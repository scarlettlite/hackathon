from collections import defaultdict
class Solution:
    def __init__(self):
        arr = [(0,2), (3,5), (6,8)]
        self.sq = [(a,b,c,d) for a,b in arr  for c,d in arr]

    def getsqr(self, ir, ic):
        for a,b,c,d in self.sq:
            if a <= ir <= b and c <= ic <= d:
                return a,b,c,d


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x == '.': continue
                if x not in rows[i]:
                    rows[i].add(x)
                else:
                    return False
                if x not in cols[j]:
                    cols[j].add(x)
                else:
                    return False
                t = self.getsqr(i, j)
                if x not in sqrs[t]:
                    sqrs[t].add(x)
                else:
                    return False
        return True
print(Solution().isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))


