from collections import defaultdict
from random import choice
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dd = defaultdict(set)
        self.vals = []
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        rval = False
        if val not in self.dd:
            rval = True
        self.vals.append(val)
        self.dd[val].add(len(self.vals) - 1)
        return rval
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        rval = False
        if val in self.dd:
            rval = True
            idx = self.dd[val].pop()
            li = len(self.vals) - 1
            if idx != li:
                """
                special case handling if there is only one element in vals
                or idx popped from the end is same as length of vals - 1
                """
                le = self.vals[li]
                self.dd[le].remove(li)
                self.dd[le].add(idx)
                self.vals[idx] = le
            if len(self.dd[val]) == 0:
                del self.dd[val]
            self.vals.pop()
        return rval

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if self.vals:
            return choice(self.vals)
        return 0