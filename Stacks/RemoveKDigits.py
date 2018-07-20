
class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return '0'
        n, i = len(num), 0
        stack = []
        while i < n:
            while k > 0 and stack and stack[-1] > num[i]:
                k -= 1
                stack.pop()
            stack.append(num[i])
            i += 1
        """
        corner cases like 1111
        """
        while k > 0:
            k -= 1
            stack.pop()
        ans = "".join(stack)
        return str(int(ans))
print(Solution().removeKdigits("10", 1))
    



            
            