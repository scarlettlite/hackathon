from collections import defaultdict
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        ns = dict()
        for i in range(n):
            ns[nums[i]] = i
        ans = []
        seen = set()
        for i in range(n):
            if nums[i] not in seen:
                for j in range(i+1,n):
                    x = -(nums[i] + nums[j])
                    if x in ns and i < ns[x] and j < ns[x] and ns[x] :
                        ans.append([nums[i], nums[j], x])
            seen.add(nums[i])
        return ans
                    
print(Solution().threeSum([-1,0,1,2,-1,-4]))