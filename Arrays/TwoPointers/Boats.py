from collections import defaultdict
class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boats = 0
        capacityleft = limit
        n = len(people)
        l, r = 0, n - 1
        people.sort()
        boatsdict = defaultdict(list)
        while l < r:
            weight = people[l] + people[r]
            if weight <= capacityleft:
                capacityleft -= weight
                l += 1 
                r -= 1
                boatsdict[boats].extend([people[l], people[r]])
            else:
                if people[r] <= capacityleft:
                    capacityleft -= people[r]
                    r -= 1
                    boatsdict[boats].extend([people[r]])
                elif people[l] <= capacityleft:
                    capacityleft -= people[l]
                    l += 1
                    boatsdict[boats].extend([people[l]])
                else:
                    boats += 1
                    capacityleft  = limit
        if l == r and l < n:
            if people[l] > capacityleft:
                boats += 1
        if capacityleft < limit:
            boats += 1
        print(sum(people), boats*50)

        return boats

print(Solution().numRescueBoats([2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10],
50))
