class Solution:
    def __init__(self):
        self.ans = []
        
    def combinations(self, comb, i):
        if i == len(comb):
            first = ''.join(comb)
            second = ""
            for x in first:
                second = self.m[x] + second
            if self.isodd:
                for y in '018':
                    self.ans.append(first+y+second)
            else:
                self.ans.append(first+second)
        else:
            for x in '01869':
                comb[i] = x
                self.combinations(comb, i+1)
                comb[i] = None
            
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        half = n//2
        self.isodd = n%2 == 1
        self.m = {'0':'0','1':'1','6':'9','9':'6','8':'8'}
        s = [None for x in range(half)]
        for x in '1869':
            s[0] = x
            self.combinations(s,1)
            s[0] = None
        return self.ans


print(Solution().findStrobogrammatic(3))