class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left = -1
        right = len(A)
        i = 0
        while i < right:
            if A[i] % 2 == 0:
                left += 1
                A[left], A[i] = A[i], A[left]
                i += 1
            else:
                right -= 1
                A[right], A[i] = A[i], A[right]
        return A

print(Solution().sortArrayByParity([1,3,0,5]))