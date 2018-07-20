class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = [asteroids[0]]
        currkilled = False
        for x in asteroids[1:]:
            #0 is positive
            while stack and stack[-1] >= 0 and x < 0 and not currkilled:
                if stack[-1] == -x:
                    currkilled = True
                    stack.pop()
                elif stack[-1] <= -x:
                    stack.pop()
                else:
                    currkilled = True
            if currkilled == True:
                currkilled = False
            else:
                stack.append(x) 
            
        return stack

print(Solution().asteroidCollision([12,10,-14,-6,9,-3]))