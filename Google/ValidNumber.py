class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        isDot, isDigit, isE = False, False, False
        for i,x in enumerate(s):
            if x == "e":
                #if e occurs before any digit or an E has already been seen
                if not isDigit or isE:
                    return False
                # set digit = false to ensure that a digit occurs at the end
                isDigit = False
                isE = True
            elif x in "+-":
                # +- can occur either at the first idx or just before an e
                if i != 0 and s[i-1] != "e": 
                    return False
            elif x == ".":
                #there will be no dots or Es after .
                if isDot or isE :
                    return False
                isDot = True
            elif x.isdecimal():
                isDigit = True
            else:
                return False

        return len(s) > 0 and isDigit;

print(Solution().isNumber("52e+9"))
