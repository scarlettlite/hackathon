"""
https://leetcode.com/problems/1-bit-and-2-bit-characters/
"""
class Solution:
    def helper(self, bits, index):
        if index < 0:
            if index == -1:
                return True
        else:
            if index > 0 and bits[index] == 1 and bits[index-1]:
                return self.helper(bits, index-2)
            elif bits[index] == 0:
                if self.helper(bits, index-1) == True:
                    return True
                elif index > 0 and bits[index-1] == 1:
                    if self.helper(bits, index-2) == True:
                        return True
        return False

    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if bits[-1] != 0:
            return False
        return self.helper(bits, len(bits) - 2)

print(Solution().isOneBitCharacter([1,0,0,0,0,1,1,0,0]))
