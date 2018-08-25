class Solution(object):
    def checkPossibility(self, A):
        p = None
        for i in range(1, len(A)):
            if A[i-1] > A[i]:
                if p != None:
                    return False
                else:
                    p = i

        if p == 1 or p == len(A) - 1 or A[p-1] <= A[p+1] or A[p-2] <= A[p]:
            return True
        return False
        
print(Solution().checkPossibility([2,3,3,2,4]))