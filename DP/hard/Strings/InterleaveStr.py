"""
"""
from collections import defaultdict
class Solution:
    def __init__(self):
        self.visited = defaultdict(bool)

    def isInterleave(self, s1, s2, s3):
        if (s1,s2,s3) in self.visited :
            return self.visited[(s1,s2,s3)]
        if not s1 and not s2 and not s3: return True
        result = False
        for i in range(len(s1)):
            if s1[:i+1] == s3[:i+1]:
                result = result or self.isInterleave(s2, s1[i+1:], s3[i+1:])
                self.visited[(s1,s2,s3)] = result
                if result == True: return result
            else:
                break
        
        for i in range(len(s2)):
            if s2[:i+1] == s3[:i+1]:
                result = result or self.isInterleave(s1, s2[i+1:], s3[i+1:])
                self.visited[(s1,s2,s3)] = result
                if result == True: return result
            else:
                break
        
        return False


print(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc"))