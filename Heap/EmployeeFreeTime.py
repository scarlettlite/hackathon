class Solution(object):
    def employeeFreeTime(self, avails):
        OPEN, CLOSE = 0,1
        events = []
        for a in avails:
            for x in a:
                events.append((x.start, OPEN))
                events.append((x.end, CLOSE))
        events.sort()
        ans, prev, balance = [], None, 0
        for t, state in events:
            if balance == 0 and prev != None:
                ans.append(prev, t)
            if state == OPEN: 
                balance += 1
            else:
                balance -= 1
            prev = t
        return ans

Solution().employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]])