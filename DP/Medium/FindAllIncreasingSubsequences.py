class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for x in nums:
            temp = []
            for a in ans:
                if a[-1] <= x:
                    temp.append(a[:] + [x])
            ans.extend(temp) 
            ans.append([x])
        a2 = []
        for a in ans:
            if len(a) > 1:
                a2.append(a)
        return a2

print(Solution().findSubsequences([4,6,7,7]))