from heapq import heappush, heappop
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = sorted([(L,-H,R) for L,R,H in buildings] + [(R,0,None) for L,R,H in  buildings])
        heap = [(0,float('inf'))]
        ans = []
        for l, negH, r in events:
            while heap and heap[0][1] <= l:
                heappop(heap)
            if negH != 0:
                heappush(heap, (negH, r))
            if not ans or ans[-1][1] != heap[0][0]:
                ans.append([l, -heap[0][0]])
        return ans

print(Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))