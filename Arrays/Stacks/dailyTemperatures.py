class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if not temperatures: return 0
        n = len(temperatures)
        """
        if adding indoces to the stack , adding -1 
        may help in writing less code
        """
        stack = [-1]
        ans = [0 for _ in range(n)]
        for i,x in enumerate(temperatures):
        """
        if the current temperature is greater than the stack.top()
        then pop the stack and update the number of days for the popped 
        index
        """
            while stack[-1] != -1 and x > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            else:
                stack.append(i)
        """
        At the end the stack may not be empty because for some temperatures
        we may not see a greater value in the array
        """
        return ans

print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))