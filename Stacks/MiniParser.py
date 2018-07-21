class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        ans = None
        stack = []
        num = ""
        for x in s:
            if x == '[':
                stack.append(x)
            elif x == ',':
                if num :stack.append(NestedInteger(int(num)))
                num = ""
            elif x in set('-0123456789'):
                num += x
            elif x == ']':
                if num: 
                    stack.append(NestedInteger(int(num)))
                    num = ""
                res = NestedInteger()
                temp = []
                while stack[-1] != '[':
                    temp.append(stack.pop())
                stack.pop() 
                for x in temp[::-1]:
                    res.add(x)
                stack.append(res)
        if num: 
            ans = NestedInteger(int(num))
        else:
            ans = stack[0]
        return ans
        