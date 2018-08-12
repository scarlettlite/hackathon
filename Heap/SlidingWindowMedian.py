from heapq import heappushpop, heappop, heappush
class Solution(object):
    def findMedian(self, maxheap, minheap, k):
        """
        :rtype: float
        """
        ans = None
        if (k) % 2 == 1:
            ans = float(-maxheap[0][0])
        else:
            ans = float(-maxheap[0][0] + minheap[0][0])/2
        return ans
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        lhs, rhs, medians = [], [], []
        """
        in case of sliding window, also insert the index 
        so that deleting obsolete values is easy
        """
        for i,x in enumerate(nums[:k]):
            heappush(lhs, (-x, i))
        rr = k-k//2 -1 if k & 1 else k-k//2
        for i in range(rr):
            x, i = heappop(lhs)
            heappush(rhs, (-x, i))
        for i in range(k, len(nums)+1):
            medians.append(self.findMedian(lhs, rhs, k))
            if i >= len(nums): break
            x = nums[i]
            if x >= rhs[0][0]:
                heappush(rhs, (x, i))
                #if the number to be deleted is in lhs then
                #lhs is unbalanced. Balance it
                if nums[i-k] <= rhs[0][0]:
                    y, j = heappop(rhs)
                    heappush(lhs, (-y, j))
            else :
                heappush(lhs, (-x, i))
                #if the number to be deleted is in rhs then
                #rhs is unbalanced. Balance it
                if nums[i-k] >= rhs[0][0]:
                    y, j = heappop(lhs)
                    heappush(rhs, (-y, j))
            
            while lhs[0][1] <= i-k: heappop(lhs)
            while rhs[0][1] <= i-k: heappop(rhs)
        return medians

print(Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 4))  


