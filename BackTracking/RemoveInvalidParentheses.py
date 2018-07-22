from collections import deque
class Solution:
    def __init__(self):
        self.visited = set()
        self.ans = []
        
    def isValidParentheses(self,s):
        count = 0
        for x in s:
            if x == '(':
                count += 1
            if x == ')':
                count -= 1
            if count < 0:
                break
        return count == 0
             
    def helper(self, s):
        queue = deque([s])
        self.visited.add(s)

        while queue and len(self.ans) == 0:
            size = len(queue)
            for _ in range(size):
                string = queue.popleft()
                if not self.isValidParentheses(string) and len(self.ans) == 0:
                    for i,x in enumerate(string):
                        if x in '()':
                            news = string[:i] + string[i+1:]
                            if news not in self.visited:
                                self.visited.add(news)
                                queue.append(news)
                elif self.isValidParentheses(string) == True:
                    self.ans.append(string)

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.helper(s)
        return self.ans

Solution().removeInvalidParentheses(")(")