class MyCalendarTwo:

    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i,j in self.overlaps:
            if not (j <= start or end <= i):
                return False

        for i,j in self.calendar:
            if not (j <= start or end <= j):
                self.overlaps.append((max(start,i), min(end,j)))

        self.calendar.append((start, end))
        return True
            

        
cal = MyCalendarTwo();
cal.book(47, 50); 
cal.book(1, 10); 
cal.book(27, 36); 
cal.book(40, 47); 
cal.book(20, 27); 
cal.book(15, 23);
cal.book(10, 18); 
cal.book(27, 36); 
cal.book(17, 25); 
cal.book(8, 17);
