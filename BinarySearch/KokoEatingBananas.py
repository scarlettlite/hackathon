class Solution(object):
    def isGreater(self, piles, H, k):
        n = len(piles)
        totalPiles = 0
        for i in range(n-1, -1, -1):
            x,y = divmod(piles[i], k)
            if y > 0:
                x += 1
            totalPiles += x
        return totalPiles <= H
            
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        piles.sort()
        low, high = 1, piles[-1]
        while low < high:
            mid = (low + high) // 2
            result = self.isGreater(piles, H, mid) 
            #print(H, mid, result)
            if result == False:
                low = mid + 1
            else:
                high = mid
        return low

print(Solution().minEatingSpeed([30,11,23,4,20],
6
))