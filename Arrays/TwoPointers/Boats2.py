from collections import defaultdict
class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boats = 0
        n = len(people)
        l, r = 0, n - 1
        people.sort()
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            boats += 1
            r-=1
        return boats