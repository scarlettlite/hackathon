import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        heap = list(zip(matrix[0], [0 for i in range(n)], [i for i in range(n)]))
        heapq.heapify(heap)
        x = 0
        while x < k:
            x += 1
            val, row, col = heapq.heappop(heap)
            if row + 1< n:
                heapq.heappush(heap, (matrix[row+1][col],row+1,col))
        return val

print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]],))