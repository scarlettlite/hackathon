from heapq import heappush, heappop, heapify
class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums: return -1
        heap = []
        minrange = float('inf')
        maxvalue = float('-inf')
        for i, l in enumerate(nums):
            if l:
                heap.append((l[0], i, 1))
                if l[0] > maxvalue:
                    maxvalue = l[0]
        
        heapify(heap)
        minrange = maxvalue - heap[0][0]
        while True:
            num, lidx, idx = heappop(heap)
            if idx < len(nums[lidx]):
                x = nums[lidx][idx] 
                heappush(heap, (nums[lidx][idx], lidx, idx+1))
                maxvalue = max(x, maxvalue)
                minrange = min(minrange, maxvalue - heap[0][0])
            else:
                break
        return minrange

print(Solution().smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))


