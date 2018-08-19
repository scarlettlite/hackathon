import heapq

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def printme(self):
        print(self.start, self.end)


class Solution(object):
    def employeeFreeTime(self, avails):
        ans = []
        pq = [(emp[0].start, ei, 0) for ei, emp in enumerate(avails)]
        heapq.heapify(pq)
        anchor = min(iv.start for emp in avails for iv in emp)
        while pq:
            t, e_id, e_jx = heapq.heappop(pq)
            if anchor < t:
                ans.append(Interval(anchor, t))
            anchor = max(anchor, avails[e_id][e_jx].end)
            if e_jx + 1 < len(avails[e_id]):
                heapq.heappush(pq, (avails[e_id][e_jx+1].start, e_id, e_jx+1))

        return ans
arr = [[Interval(1,3), Interval(6,7)],[Interval(2,4)],[Interval(2,5),Interval(9,12)]]
for x in Solution().employeeFreeTime(arr):
    x.printme()
