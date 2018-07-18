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
            if stack :
                t1 = int(stack[-1].split(':')[-1])
                t2 = int(log.split(':')[-1])
                if "end" in log and "start" in stack[-1]:
                    p = int(log.split(':')[0])
                    if prev :
                       t3 = int(prev.split(':')[-1])
                       ans[p] += t2 - t3
                    else:
                        ans[p] += t2 - t1 + 1
                    prev = log
                    stack.pop()
                elif "start" in log:
                    p = int(stack[-1].split(':')[0])
                    if prev :
                       t3 = int(prev.split(':')[-1])
                       ans[p] += t2 - t3 - 1
                       prev = None
                    else:
                       ans[p] +=  t2 -  t1 
                    stack.append(log)
            else:
                stack.append(log)
        return ans

print(Solution().exclusiveTime(1,
["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
))

        
       
