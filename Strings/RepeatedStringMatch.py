class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        x = len(B) // len(A) + 2
        for i in range(x):
            if( B in A * (i+1)):
                return i + 1
        return -1

print(Solution().repeatedStringMatch("abc", "cabcabca"))