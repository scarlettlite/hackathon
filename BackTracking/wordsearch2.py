class Solution:
    def __init__(self):
        self.root ={}
        self.ans = set()
        self.visited = None
        
    def createtrie(self, words):
        for word in words:
            if word == "":
                continue
            curr = self.root
            for ch in word:
                curr = curr.setdefault(ch, {})
            curr['value'] = word
                
    def findPrefix(self, prefix):
        curr = self.root
        for ch in prefix:
            if curr.get(ch) == None:
                return "Not Found"
            curr = curr.get(ch)
        if curr.get('value') == prefix:
            return "Word Found"
        else:
            return "Prefix found"

    
    def backtrack(self,board,r,c,word):
        if self.visited[r][c] == False:
            nw = word+board[r][c]
            res = self.findPrefix(nw)
            if res != "Not Found":
                if res == "Word Found":
                    self.ans.add(nw)
                self.visited[r][c] = True
                m = len(board)
                n = len(board[r])
                if r+1 < m:
                    self.backtrack(board,r+1,c,nw)
                if c+1 < n:
                    self.backtrack(board,r,c+1, nw)
                if c-1 >= 0:
                    self.backtrack(board,r,c-1, nw)
                if r-1 >= 0:
                    self.backtrack(board,r-1,c, nw)
                self.visited[r][c] = False
                            
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not words: return []
        self.createtrie(words)
        m = len(board)
        n = len(board[0])
        self.visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                self.backtrack(board, i, j, "")

        return self.ans

print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
, ["oath","pea","eat","rain", "eath"]))
        