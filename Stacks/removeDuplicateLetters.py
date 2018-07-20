from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s : return s
        stack=[]
        c = Counter(s)
        sa = set()
        for x in s:
            while stack and  stack[-1] > x and c[stack[-1]] > 0:
                if x not in sa:
                    y = stack.pop()
                    sa.remove(y)
                else:
                    c[x] -= 1
                    break
            else:
                if x not in sa:
                    sa.add(x)
                    stack.append(x)
                c[x] -= 1
        return ''.join(stack)

#param = Solution().removeDuplicateLetters("hakalmmhlk")
#param2 = Solution().removeDuplicateLetters("ababsdfgsfdg")
param3 = Solution().removeDuplicateLetters("aallddyy")
#print(param, param2)

#"ababsdfgsfdg"