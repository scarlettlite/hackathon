from bisect import bisect_left
class Meeting():
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        return self.end <= other.start

    def __eq__(self, other):
        return self.start <= other.start < self.end or self.start < other.end < self.end \
        or other.start <= self.start <= self.end <= other.end

    def __str__(self):
        return "start:" + str(self.start) + " end:" + str(self.end)
    
    
class MyCalendar:

    def __init__(self):
        self.meetings = []

    def canmakeappointment(self, oldmeeting, newmeeting):
        if oldmeeting.start <= newmeeting.start < oldmeeting.end or oldmeeting.start < newmeeting.end < oldmeeting.end \
        or newmeeting.start <= oldmeeting.start <= oldmeeting.end <= newmeeting.end:
            return False
        return True

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if start >= end: return False
        newmeeting = Meeting(start, end)
        if not self.meetings:
            self.meetings.append(newmeeting)
        else:
            idx = bisect_left(self.meetings, newmeeting)
            if idx == len(self.meetings) or self.meetings[idx] != newmeeting:
                self.meetings.insert(idx, newmeeting)
            else:
                return False
        return True
      

cal = MyCalendar()
cal.book(47,50)
cal.book(33,41)
cal.book(39,45)
cal.book(33,42)
cal.book(25,32)
cal.book(26,35)
cal.book(19,25)
cal.book(3,8)
cal.book(8,13)
cal.book(18,35)

for m in cal.meetings:
    print(m)