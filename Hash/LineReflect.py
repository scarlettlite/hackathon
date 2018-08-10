class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        midx = (min([x for x, y in points]) + max([x for x, y in points])) / 2.0
        s = set()
        for x, y in points:
            s.add((x,y))
        for x, y in points:
            if (2 * midx - x, y) not in s:
                return False
        return True