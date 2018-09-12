class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3: return 0
        maxlength = 0
        i, n = 1, len(A)
        while i < n:
            incr, dcr, equal = 0, 0, 0
            while i < n and A[i-1] < A[i]:
                incr += 1
                i += 1
            while i < n and A[i-1] == A[i]:
                equal += 1
                i += 1
            while i < n and A[i-1] > A[i]:
                dcr += 1
                i += 1
            if incr > 0 and dcr > 0 and equal == 0:
                maxlength = max(maxlength, incr + dcr + 1)

        return maxlength
            
            
print(Solution().longestMountain([]))