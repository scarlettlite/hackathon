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
        for log in logs:
            if stack and stack[-1].startswith(log[0]):
                obj = stack.pop()
                p,s,t = obj.split(':')
                p, t = int(p), int(t)
                p1,s1,t1 = log.split(':')
                p1, t1 = int(p1), int(t1)
                et = (t1 - t) + 1
                ans[p] += et
                if stack:
                    obj = stack[-1]
                    ans[int(obj[0])] -= et               
            else:
                stack.append(log)
        return ans

print(Solution().exclusiveTime(4,
["0:start:0",
 "1:start:2",
 "1:end:5",
 "2:start:7",
 "3:start:8",
 "3:stop:10",
"2:stop:14",
 "0:end:16"]
))

        
       
