from collections import OrderedDict, deque
class Solution:
    def helper(self, bits):
        li = len(bits) - 1
        stack = [[bits, li]]
        seen = OrderedDict()
        seen[0] = True
        ll = pow(2, len(bits))
        while stack and len(seen) < ll:
            bits, i = stack[-1]
            if i > -1:
                y = bits[i]
                if bits[i] == '0':
                    bits[i] = '1'
                else:
                    bits[i] = '0'
                x = int(''.join(bits), 2)
                stack[-1][-1] -= 1
                if x not in seen:
                    stack.append([bits[:], li])
                    seen[x] = True
                bits[i] = y
            else:
                stack.pop()
        return list(seen.keys())
        
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        return self.helper(['0']*n)

print(Solution().grayCode(10))
