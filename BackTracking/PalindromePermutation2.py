class Solution(object):
    def helper(self, a, i, ans):
        n = len(a)
        if i == n:
            ans.add(''.join(a))
        else:
            for j in range(i,n):
                a[i], a[j] = a[j], a[i]
                if j < n//2 or (j >= n//2 and a[j] == a[n-j-1]):
                    self.helper(a, i+1, ans)
                a[i], a[j] = a[j], a[i]


    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = set()
        self.helper(list(s), 0, ans)
        return (list(ans))


print(Solution().generatePalindromes("aabb"))

