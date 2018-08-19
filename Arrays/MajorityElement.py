"""

"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dd = {}
        ans = []
        for x in nums:
            if x in dd:
                dd[x] += 1
            else:
                dd[x] = 1
            if len(dd) == 3:
                remove = []
                for key in dd.keys():
                    dd[key] -= 1
                    if dd[key] == 0:   
                        remove.append(key)
                for x in remove:
                    del dd[x]
                
        for x in dd.keys():
            if nums.count(x) > len(nums) // 3:
                ans.append(x)
        return ans

print(Solution().majorityElement([1,2,3,1,1,3,1,2,3]))