class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if not n or not logs: return []
        ans = [ 0 for _ in range(n)]
        stack = []
        prev = None
        for log in logs:
            curr = log.split(':')
            """
            prev always behaves like a start time
            so if an end time is folowed by another end time,
            prev is incremented by 1 to make it a start time of 
            the next process
            Instead of looking at the whole process look at each log 
            as a separate piece of execution
            """
            if stack :
                if "end" in log :
                    ans[stack[-1]] += int(curr[2]) - prev + 1
                    stack.pop()
                    prev = int(curr[2]) + 1
                else:
                    ans[stack[-1]] += int(curr[2]) - prev
                    stack.append(int(curr[0]))
                    prev = int(curr[2]) 
            else:
                stack.append(int(curr[0]))
                prev = int(curr[2])
        return ans

print(Solution().exclusiveTime(2,
["0:start:0","1:start:2","1:end:5","0:end:8"]
))

        
       
