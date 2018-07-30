from collections import defaultdict
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        dd = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                dd[(nums[i] + nums[j])].append((i,j))
                
        ans = []
        seen = set()
        for key, value in dd.items():
            y = target - key
            if key not in seen and y in dd:
                seen.add(y)
                vl = dd[y]
                for a,b in value:
                    for c,d in vl:
                        if a != c and a!= d and b != c and b != d:
                            ans.append(sorted([nums[a], nums[b], nums[c], nums[d]]))
        
        return ans
                
Solution().fourSum([1, 0, -1, 0, -2, 2],3)