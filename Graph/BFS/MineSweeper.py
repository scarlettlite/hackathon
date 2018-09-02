class Solution:
    def dfs(self, board, start, visited):
        if start not in visited:
            m, n = len(board), len(board[0])
            r,c = start
            visited.add(start)
            if board[r][c] == 'M':
                board[r][c] = 'X'
            elif board[r][c] == 'E':
                directions = ((1, 0), (-1, 0), (0, 1), (0, -1), (1,1), (-1,-1), (1,-1), (-1, 1))
                mines = 0
                neighbors = []
                for i, j in directions:
                    ir, ic = start
                    ir += i
                    ic -= j
                    if 0 <= ir < m and 0 <= ic < n:
                        if board[ir][ic] == 'M' or board[ir][ic] == 'X':
                            mines += 1
                        neighbors.append((ir,ic))
                if mines > 0:
                    board[r][c] = str(mines)
                else:
                    board[r][c] = 'B'
                    for n in neighbors:
                        self.dfs(board, n, visited)

            
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        self.dfs(board, tuple(click), set())
        return board

print(Solution().updateBoard([['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']], [1,1]))
