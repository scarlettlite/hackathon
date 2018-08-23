"""
https://leetcode.com/problems/restore-ip-addresses/
"""
class Solution:
    def helper(self, path, index, dots):
        ans = []
        if dots == 3:
            ipaddr = ''.join(path)
            tokens = ipaddr.split('.')
            """
            be careful with it. it will throw exception for non integer strings
            """
            if all (int(x) <= 255 and str(int(x)) == x for x in tokens):
                ans.append(ipaddr)
            #print(ipaddr, tokens)
        elif index == len(path):
            pass
        else:
            path[index] = '.'
            ans.extend(self.helper(path, index + 2, dots + 1))
            path[index] = ''
            ans.extend(self.helper(path, index + 2, dots))
        return ans

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        """
        if n == 0, len of path became negative
        """
        path = [None] * (2*n - 1)
        path[::2] = s
        path[1::2] = [""] * (n-1)
        return self.helper(path, 1, 0)

print(Solution().restoreIpAddresses("010110011"))
