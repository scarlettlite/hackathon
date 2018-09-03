class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n, l, r = len(s), 0, len(s)-1
        while l < r:
            while l < n and not s[l].isalnum():
                l += 1
            while r > -1 and not s[r].isalnum():
                r -= 1
            if l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))