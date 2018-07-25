class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operator, operand = [], []
        priority = 0
        num = ""
        for x in s:
            """
            brackets have the largest priority
            """
            if x == '(':
                priority += 10
            elif x == ')':
                """
                reduce priority when we see a closed bracket
                so that operation inside the brackets get evaluated 
                first
                """
                priority -= 10
                """A number may finish here"""
                if num: 
                    operand.append(int(num))
                    num = ""
            """
            Question is for non - negative integers only
            """
            elif x in set('0123456789'):
                num += x
            elif x in set('+-*/'):
                """A number may finish here"""
                if num: 
                    operand.append(int(num))
                    num = ""
                newpriority = priority
                if x in '*/':
                    """ * and / have more priority than + and -
                    but less priority than brackets """
                    newpriority += 1
                    """
                    do not increase the overall priority because we may see
                    + or - after * or /
                    """
                while operator and operator[-1][1] >= newpriority:
                    self.calculatetop(operator, operand)
                operator.append((x, newpriority))

        """
        incorporate the number that is left
        """
        if num: 
            operand.append(int(num))
        while operator:
            self.calculatetop(operator, operand)
        return operand[0]

    def calculatetop(self, operator, operand):
        second, first = operand.pop(), operand.pop()
        optr = operator.pop()[0]
        res = 0
        if optr == '+':
            res = first + second
        elif optr == '-':
            res = first - second
        elif optr == '*':
            res = first * second
        elif optr == '/':
            res = first / second
        operand.append(res)


print(Solution().calculate("1+5*2/5"))