class Solution:
    def __init__(self):
        self.cache = []

    def canbeplaced(self, queens, r, c):
        for i,x in enumerate(queens):
            if x == c or abs(i-r) == abs(x-c):
                return False
        return True


    def helper(self, queens, k, n):
        if n == k:
            self.cache.append(queens[::])
        else:
            for c in range(n):
                if self.canbeplaced(queens, k, c):
                    queens.append(c)
                    self.helper(queens, k+1, n)
                    queens.pop()

    def getOutput(self):
        result = []
        for arr in self.cache:
            temp = []
            for x in arr:
                string = ""
                for i in range(len(arr)):
                    if i == x:
                        string += 'Q'
                    else:
                        string += '.'
                temp.append(string)
            result.append(temp)
        return result


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.helper([], 0, n)
        return self.getOutput();

print(Solution().solveNQueens(8))