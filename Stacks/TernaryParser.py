class Solution:
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        expression = expression[::-1]
        stack = []
        prev = None
        num = ""
        for x in expression:
            if x in 'TF' and prev == '?':
                a = stack.pop()
                b = stack.pop()
                result = a
                if x == 'F':
                    result = b
                stack.append(result)
                prev = None
            elif x == '?':
                prev = '?'
                if num : stack.append(num[::-1])
                num = ""
            elif x.isdigit():
                num += x
            elif x == ':':
                if num: stack.append(num[::-1])
                num = ""
            elif x in 'TF':
                stack.append(x)
        return stack[0]
                    
param = Solution().parseTernary("T?F?T:5:T?T:F")
print(param)
