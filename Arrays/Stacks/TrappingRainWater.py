class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height : return 0
        n = len(height)
        leftmax = [-1 for _ in range(n)]
        rightmax = [-1 for _ in range(n)]
        leftmax[0] = height[0]
        #compute max number on the left side of the current number
        for i in range(1,n):
            leftmax[i] = max(leftmax[i-1], height[i])

        #compute max number on the right side of the current number
        rightmax[-1] = height[-1]
        for i in range(n-2,-1,-1):
            rightmax[i] = max(rightmax[i+1], height[i])
        ans = 0
        for i in range(1,n-1):
            ans += min(leftmax[i], rightmax[i]) - height[i]
        return ans

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
            
