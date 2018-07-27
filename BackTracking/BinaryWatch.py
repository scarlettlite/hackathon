class Solution(object):
    def getPowerSum(self, LED):
        s = 0
        for i,x in enumerate(LED):
            s += (pow(2,i) * x)
        return s


    def getValidValues(self, n, LED, i, maxvalue):
        validvalues = []
        if n == 0:
            val = self.getPowerSum(LED)
            if val <= maxvalue:
                validvalues.append(val)
        elif i < len(LED):
            validvalues.extend(self.getValidValues(n, LED, i+1, maxvalue))
            LED[i] = 1
            validvalues.extend(self.getValidValues(n-1, LED, i+1, maxvalue))
            LED[i] = 0
        return validvalues

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        vt = []
        for i in xrange(0,num+1):
            j = num - i
            if 0 <= j <= 5:
                vm = self.getValidValues(j, [0 for _ in range(6)], 0, 59)
                vh = self.getValidValues(i, [0 for _ in range(4)], 0, 11)
                for x in sortvh:
                    for y in vm:
                        vt.append("{}:{:02d}".format(x,y))
        return vt


print(Solution().readBinaryWatch(2))
