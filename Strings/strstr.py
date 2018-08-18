class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle : return 0
        if not haystack and needle : return -1
        i, m, n = 0, len(haystack), len(needle)
        for i in range(m-n+1):
            j = i
            k = 0
            while k < n and needle[k] == haystack[j]:
                k += 1
                j += 1
            if k == n:
                return i
        return -1

print(Solution().strStr("hellollo", "llo" ))