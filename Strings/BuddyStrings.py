class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B) : return False
        i = 0
        x,y = -1, -1
        for j,(a,b) in enumerate(zip(A,B)):
            if a != b:
                if i == 2:
                    return False
                else:
                    i += 1
                    if x == -1:
                        x = j
                    else:
                        y = j
        if x > -1 and y > -1 and A[x] == B[y] and A[y] == B[x]:
            return True
        if len(A) == 2 and A[0] == A[1] and B[0] == B[1] and A[0]==B[0]:
            return True
        return False

print(Solution().buddyStrings("abab", "abab"))