from collections import Counter
class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        c = Counter()
        atom = ""
        num = 1
        stack = []
        prev = None
        # ignore empty atoms
        for x in formula:
            if x.isdecimal():
                if type(prev) != int:
                    num = int(x)
                else:
                    num = num * 10 + int(x)
                prev = int(x)
            elif x.isalpha():
                if x.islower():
                    atom += x
                else:
                    stack.append([atom, num])
                    atom = x
                    num = 1
                prev = x
            elif x == '(':
                stack.append([atom, num])
                atom = ""
                num = 1
                prev = x
            elif x == ')':
                prev = x
                st = []
                stack.append([atom, num])
                atom = ""
                num = 1
                while stack[-1] != '(':
                    y = stack.pop()
                    y[1] *= num
                    st.append(y)
                stack.pop()
                stack.extend(st[::-1])

        for x in stack:
            if x[0]:
                c[x[0]] += x[1]
        
        formula = ""
        for key, value in c.items():
            formula += key
            if value > 1:
                formula += str(value)
        return formula


param  = Solution().countOfAtoms("Mg(OH)2")
print(param)



