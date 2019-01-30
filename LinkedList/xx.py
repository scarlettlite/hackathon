from string import ascii_lowercase
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if not A:
            return 0
        M = pow(10, 9) + 7
        n = len(A)
        prefix = [0]*n
        i = 0
        for j in range(1, n):
            if A[i] == A[j]:
                prefix[j] = prefix[j-1] + 1
                i += 1
            else:
                i = 0
        result = 1
        ss = 0
        for i in range(n):
            ss = (ss + ord(A[i]) - ord('a') + 1)%M
            result = (result * ss)%M
    
        

        for i in range(1,n):
            ss = 0
            j = i
            if A[i] == A[0]:
                while j < n and prefix[j] != 0:
                    ss = (ss + ord(A[j]) - ord('a') + 1)%M
                    result = (result * ss)%M
                    j += 1
                
        return result

print(Solution().solve("abab"))