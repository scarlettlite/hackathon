class Solution:
    def binarySearch(self, matrix, key,lowRow, highRow, lowCol, highCol):
        if not(0 <= lowRow <= highRow < len(matrix) and 0 <= lowCol <= highCol < len(matrix[0])):
            return False
        if lowRow == highRow and lowCol == highCol:
            return matrix[lowRow][lowCol] == key
        
        midRow, midCol = (lowRow + highRow)//2, (lowCol+highCol) //2
        cand = matrix[midRow][midCol]
        if cand == key:
            return True
        elif key < cand:
            return self.binarySearch(matrix, key, lowRow, midRow-1, lowCol, highCol) or self.binarySearch(matrix, key, midRow, highRow, lowCol, midCol-1)
        else:
            return self.binarySearch(matrix, key, midRow+1, highRow, lowCol, midCol) or self.binarySearch(matrix, key, lowRow, highRow, midCol+1, highCol)

        
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m,n = len(matrix), len(matrix[0])
        return self.binarySearch(matrix, target, 0,m-1, 0,n-1)

print(Solution().searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],
4
))