# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
from collections import defaultdict
from fractions import Fraction
class Solution:
    def getline(self, p1, p2):
        x1,y1 = p1.x, p1.y
        x2,y2 = p2.x, p2.y
        m = 'x'
        c = x1
        if x2 != x1:
            m = Fraction((y2-y1),(x2-x1))
            c = y1 - (m*x1)
        return (m,c)
    
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points: return 0
        n = len(points)
        lines = defaultdict(set)
        for i in range(n):
            for j in range(i+1,n):
                lines[self.getline(points[i], points[j])].update([i,j])
        maxvalue = 0
        for value in lines.values():
            maxvalue = max(len(value), maxvalue)
        return maxvalue

print(Solution().maxPoints([Point(3,1),Point(12,3),Point(3,1),Point(-6,-1)]))

#print(Solution().maxPoints([Point(0,0),Point(0,0)]))