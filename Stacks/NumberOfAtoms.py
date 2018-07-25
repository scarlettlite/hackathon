from collections import Counter
class Solution(object):
    def push(self,stack):
        """
        if an atom and a valid multiplicity exists
        """
        if self.atom:
            if self.mult:
                stack[-1][self.atom] += int(self.mult)
            else:
                stack[-1][self.atom] += 1
            self.atom = ""
            self.mult = ""
        elif self.mult:
            """
            if there is no valid atom and a valid multiplicity is 
            found that means, multiplicity followed a closed bracketed 
            formula
            """
            m = int(self.mult)
            c = stack.pop()
            for at, co in c.items():
                stack[-1][at] += co*m
            self.mult = ""

    def countOfAtoms(self, formula):
        stack = [Counter()]
        self.mult = ""
        self.atom = ""
        for x in formula:
            if x == '(':
                """ either an atom or multiplicity ended"""
                self.push(stack)
                """"push a fresh counter if an opening bracket is seen"""
                stack.append(Counter())
            elif x == ')':
                """ either an atom or multiplicity ended"""
                self.push(stack)
            elif x.isdigit():
                self.mult += x
            elif x.isupper():
                """either an atom or multiplicity ended"""
                self.push(stack)
                self.atom += x
            elif x.islower():
                self.atom += x

        """handle residual elements"""
        self.push(stack)

        """ failsafe if there are more than one counter"""
        """ popping and adding at the same time wont work"""
        while len(stack) > 1:
            x = stack.pop()
            stack[-1] += x

        ans = ""
        for a, c in sorted(stack[0].items()):
            cs = "" if c == 1 else str(c)
            ans += (a + cs)
        return ans 

print(Solution().countOfAtoms("Mg(Ar3(OH))"))
            

                

