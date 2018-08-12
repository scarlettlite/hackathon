import collections
class Solution(object):
    def isPossible(self, nums):
        count = collections.Counter(nums)
        tails = collections.Counter()
        for x in nums:
            if count[x] == 0:
                continue
            elif tails[x-1] > 0:
                tails[x-1] -= 1
                tails[x] += 1
            elif count[x+1] > 0 and count[x+2] > 0:
                count[x+1] -= 1
                count[x+2] -= 1
                tails[x+2] += 1
            else:
                return False
            count[x] -= 1
        return True

print(Solution().isPossible([1,2,3,3,4,4,5,5]))