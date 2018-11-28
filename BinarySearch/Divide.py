class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        count = 1
        value = divisor
        while 1:
            if value - dividend >= divisor:
                value = (value//2 + value)//2
                count = (count//2 + count)//2
            elif dividend - value >= divisor:
                value += value
                count += count
            else:
                if  0 <= value - dividend < divisor:
                    count -= 1
                break


        return count

print(Solution().divide(75739, 3))