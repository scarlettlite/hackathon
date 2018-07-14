class Solution:
    """
    Basic Calculator 3 : Leetcode
    """
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        s = list(s)
        stack  = []
        number = 0
        sign = 1
        for x in s:
            if x.isspace():
                continue
            elif x == '+':
                result += sign * number
                number = 0
                sign = 1
            elif x == '-':
                result += sign * number
                number = 0
                sign = -1
            elif x == '(':
                stack.append(result)
                result = 0
                stack.append(sign)
                sign = 1
            elif x == ')':
                if len(stack) >= 2:
                    result += sign*number
                    operator = stack.pop()
                    operand = stack.pop()
                    result = operand + (operator*result)
                    number = 0

            else:
                digit = int(x)
                number = number*10 + digit
        return result

print(Solution().calculate("-9-10+(23-9)-(-30)"))