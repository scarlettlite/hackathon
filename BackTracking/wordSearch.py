class Solution:
    def backtrack(self, board, r,c, word, k, visited):
        rv = False
        if board[r][c] == word[k] and visited[r][c] == False:
            visited[r][c] = True
            if k == len(word) - 1:
                rv = True
            else:
                m = len(board)
                n = len(board[r])
                if r + 1 < m:
                    rv = rv or self.backtrack(board, r+1, c, word, k+1, visited)
                    if rv == True: return True
                if c+1 <n:
                    rv = rv or self.backtrack(board, r, c+1, word, k+1, visited)
                    if rv == True: return True
                if c-1 >= 0:
                    rv = rv or self.backtrack(board, r, c-1, word, k+1, visited)
                    if rv == True: return True
                if r-1 >= 0:
                    rv = rv or self.backtrack(board, r-1, c, word, k+1, visited)
                    if rv == True: return True
            visited[r][c] = False
        return rv
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rv = False
        m = len(board)
        n = len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                rv = rv or self.backtrack(board, i, j, word, 0, visited)
                if rv == True: return True
        return rv

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
,"FSADECCBA"))
