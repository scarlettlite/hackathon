class Solution:
    def __init__(self):
        self.ispal = None
        self.ans = []
    def isPalindrome(self,i,j,s):
        ans = None
        if i <= j:
            if self.ispal[i][j] == None:
                self.ispal[i][j] = (s[i] == s[j] and self.isPalindrome(i+1, j-1, s))
            ans = self.ispal[i][j]
        else:
            ans = True
        return ans
            
    def backtrack(self, s, k, partition):
        if k == len(s):
            self.ans.append(partition[::])
        else:
            n = len(s)
            for i in range(k, len(s)):
                if self.isPalindrome(k,i,s):
                    partition.append(s[k:i+1])
                    self.backtrack(s, i+1, partition)
                    partition.pop()
        

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        l = len(s)
        self.ispal = [[True if i == j else None for j in range(l)] for i in range(l)]
        self.backtrack(s,0,[])
        return self.ans

print(Solution().partition('aabbcb'))