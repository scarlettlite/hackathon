class Solution(object):
    def helper(self,a,b,c):
        if c == "":
            return True
        val = str(int(a) + int(b))
        if c.startswith(val):
            return self.helper(b,val,c[len(val):])
        return False

    def isAdditiveNumber(self, string):
        """
        :type num: str
        :rtype: bool
        """
        n = len(string)
        result = False
        for i in range(1,n):
            for j in range(i+1,n):
                a = string[:i]
                b = string[i:j]
                c = string[j:]
                if (a.startswith('0') and a!= '0') or (b.startswith('0') and b!=0 ) or (len(c) < len(a) and len(c) < len(b)):
                    continue
                else:
                    result = self.helper(a,b,c)
                    if result == True: return result
        return result

print(Solution().isAdditiveNumber("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))