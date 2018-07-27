from collections import Counter
class Solution(object):
    def helper(self, a, i, ch):
        n = len(a)
        ans = set()
        if i == n:
            val = ''.join(a)
            ans.add(val + ch + val[::-1])
        else:
            seen = set()
            for j in range(i,n):
                if a[j] not in seen:
                    seen.add(a[j])
                    a[i], a[j] = a[j], a[i]
                    ans = ans | self.helper(a, i+1, ch)
                    a[i], a[j] = a[j], a[i]
        return ans


    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        c = Counter(s)
        ch = ""
        string = ""
        odd = 0
        for key, value in c.items():
            if value % 2 == 1:
                ch = key
                odd += 1
            string += (key * (value // 2))
        print(string)
        ans = []
        if odd < 2:
            ans = list(self.helper(list(string), 0, ch))
        return ans


print(Solution().generatePalindromes("aabbccc"))

