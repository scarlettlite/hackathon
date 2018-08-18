class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero, one = 0, 1
        count, mv, state, prevcount = 0, 0, zero, 0
        for i, x in enumerate(nums):
            if x == 1:
                count += 1
                mv = max(mv, count)
            else:
                if state == zero:
                    state = one
                    prevcount = count
                    count += 1
                    mv = max(mv, count)
                elif state == one:
                    if i > 0 and nums[i-1] == 1:
                        count = count - prevcount 
                        prevcount = count
                    else:
                        count, prevcount = 0, 0
                        state = zero
        return mv

print(Solution().findMaxConsecutiveOnes([]))