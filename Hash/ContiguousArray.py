class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        dd = {0:-1}
        ans = 0
        for i,x in enumerate(nums):
            if x == 0:
                count += 1
            else:
                count -= 1
            if count in dd:
                """
                this works like cumulayive sum so we dont
                have to do -1 here
                """
                ans = max(ans, i - dd[count])
            else:
                dd[count] = i
        return ans
print(Solution().findMaxLength([1,1,1,1,0,0,1,0,0]))
