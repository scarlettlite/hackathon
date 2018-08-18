class Solution:
    def addBinary(self, A, B):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not A or not B : return A or B
        c = '0'
        ans = []
        if len(A) < len(B):
            A, B = B, A
        B = '0'*(len(A) - len(B)) + B
        for a, b in zip(reversed(A), reversed(B)):
            if a == '1' and b == '1' and c == '1':
                ans.append('1')
                c = '1'
            elif (a == '1' and b == '1') or ((a == '1' or b == '1') and c == '1'):
                ans.append('0')
                c = '1'
            elif a == '1' or b == '1':
                ans.append('1')
                c = '0'
            elif c == '1':
                ans.append('1')
                c = '0'
            else:
                ans.append('0')
                c = '0'
        if c == '1': ans.append('1')
        return ''.join(ans[::-1])

print(Solution().addBinary("10000", "111"))