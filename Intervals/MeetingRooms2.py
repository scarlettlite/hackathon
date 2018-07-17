# Definition for an interval.
import heapq
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:

    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x: x.start)
        heap, time, rooms = [], 0, 0
        for intr in intervals:
            """
            we keep the meeting whose end time is minimum at the top
            so that when ever we see a start time more than current top 
            end time in heap, then that meeting can use the same room as 
            this current top. So pop that out and insert this mew meeting 
            in its place. In some cases we may pop out more than one 
            meetingthat means that the new meeting could take place in 
            any of those rooms occupied by the meeting that just popped. 
            The length of the heap will increase only when we can no 
            longer use the existing rooms. When that happens, increment
            the rooms by one
            """
            while heap and heap[0] <= intr.start:
                heapq.heappop(heap)
            heapq.heappush(heap, intr.end)
            if len(heap) > rooms:
                rooms += 1
        return rooms
l = [Interval(9,10), Interval(4,9), Interval(4,17), Interval(3,7), Interval(11,14)]
print(Solution().minMeetingRooms(l))