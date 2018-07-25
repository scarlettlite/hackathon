class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operator, operand = [], []
        priority = 0
        num = ""
        for  x in s:
            if x.isdigit():
                num += x
            elif x in set('+-/*'):
                if num:
                    operand.append(int(num))
                    num = ""
                newpriority = priority
                if x in '/*':
                    newpriority += 1
                while operator and operator[-1][1] >= newpriority:
                    self.calculatetop(operator, operand)
                operator.append((x, newpriority))

        """
        take care of residual numbers
        """
        if num:
            operand.append(int(num))

        while operator:
            self.calculatetop(operator, operand)

        return operand[0]

    def calculatetop(self, operator, operand):
        second, first = operand.pop(), operand.pop()
        optr = operator.pop()[0]
        result = 0
        if optr == '/':
            result = first // second
        elif optr == '-':
            result = first - second
        elif optr == '*':
            result = first * second
        elif optr == '+':
            result = first + second
        operand.append(result)

print(Solution().calculate('1+1-4+0*6'))

