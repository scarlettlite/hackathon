from collections import defaultdict
class Solution:
    def __init__(self):
        arr = [(0,2), (3,5), (6,8)]
        self.sqs = [(a,b,c,d) for a,b in arr for c,d in arr]

    def getsqr(self, ir, ic):
        for a,b,c,d in self.sqs:
            if a <= ir <= b and c <= ic <= d:
                return a, b, c, d

    def helper(self, board, ir, ic, rows, cols, sqrs):
        if ir == len(board) and ic == 0:
            return True
        else:
            try:
                if board[ir][ic] == '.':
                    for x in list('123456789'):
                        cond = x not in rows[ir] and x not in cols[ic]
                        cond &= x not in sqrs[self.getsqr(ir, ic)]
                        if cond:
                            board[ir][ic] = x
                            rows[ir].add(x)
                            cols[ic].add(x)
                            sqrs[self.getsqr(ir,ic)].add(x)
                            nr = ir if ic + 1 < len(board[ir]) else ir + 1
                            nc = ic + 1 if ic + 1 < len(board[ir]) else 0
                            result = self.helper(board, nr, nc, rows, cols, sqrs)
                            if result == True:
                                return True
                            board[ir][ic] = '.'
                            rows[ir].remove(x)
                            cols[ic].remove(x)
                            sqrs[self.getsqr(ir,ic)].remove(x)
                else:
                    nr = ir if ic + 1 < len(board[ir]) else ir + 1
                    nc = ic + 1 if ic + 1 < len(board[ir]) else 0
                    return self.helper(board, nr, nc, rows, cols, sqrs)
            except:
                print(ir, ic)
        return False
                    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                rows[i].add(x)
                cols[j].add(x)
                sqrs[self.getsqr(i,j)].add(x)

        self.helper(board, 0, 0, rows, cols, sqrs)
        return
print(Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))


