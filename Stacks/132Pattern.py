class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3: return False
        n = len(nums)
        """
        For each element in the array track the minimum value seen 
        upto that element
        """
        minn = [nums[0] for _ in range(n)]
        for i in range(1,n):
            x = nums[i]
            if x < minn[i-1]:
                minn[i] = x
            else:
                minn[i] = minn[i-1]
        stack = []
        for i in range(n-1, -1, -1):
            m = minn[i]
            x = nums[i]
            """
            we begin from back of the array. We are trying to find a value
            which lies in the middle of x and m. So we pop out all the values
            that are less than equal to m. If the next greater value than m 
            is smaller than x then that means we have found our 132 pattern
            """
            while stack and stack[-1] <= m:
                stack.pop()
            if stack and stack[-1] < x:
                return True
            stack.append(x)

        return False


print(Solution().find132pattern([6,12,3,4,6,11,20]))
            