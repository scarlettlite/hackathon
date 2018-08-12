from heapq import heappush, heappop, heappushpop
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        """
        Always insert in maxheap and then balance them later
        """
        x = heappushpop(self.maxheap, -num)
        heappush(self.minheap, -x)
        if len(self.maxheap) < len(self.minheap):
            y = heappop(self.minheap)
            heappush(self.maxheap, -y)
        

    def findMedian(self):
        """
        :rtype: float
        """
        a, b = len(self.minheap), len(self.maxheap)
        ans = None
        if (a + b) % 2 == 1:
            ans = float(-self.maxheap[0])
        else:
            ans = float(-self.maxheap[0] + self.minheap[0])/2
        return ans