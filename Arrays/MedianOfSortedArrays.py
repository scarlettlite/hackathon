class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x, y = len(nums1), len(nums2)
        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)
        
        low, high = 0, x
        
        while low <= high:
            partitionX = (low+high)//2
            partitionY = (x+y+1)//2 - partitionX
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX-1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY-1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            print(maxLeftX, minRightX, maxLeftY, minRightY)
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if ((x+y) % 2 == 0):
                    return (max(maxLeftY,maxLeftY) + min(minRightY+minRightX))/2
                else:
                    return float(max(maxLeftX, maxLeftY))
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1

print(Solution().findMedianSortedArrays([1,3],[2]))