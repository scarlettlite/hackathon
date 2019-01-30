"""
Used in Questions where we want 
to find minimum, maximum, sum, in a rannge,
"""
from math import log2, ceil
class SegmentTree:
    def __init__(self, input):
        self.n = len(input)
        x = ceil(log2(self.n))
        k = 2 * pow(x, 2) - 1
        self.tree = [0] * k
        self.construcTree(input, 0, self.n-1, 0)


    def construcTree(self, input, low, high, pos):
        if low < len(input) and low == high:
            self.tree[pos] = input[low]
            return

        mid = (low + high) // 2
        leftChild = 2*pos + 1
        rightChild = 2*pos + 2
        self.construcTree(input, low, mid, leftChild)
        self.construcTree(input, mid+1, high, rightChild)
        self.tree[pos] = min(self.tree[leftChild], self.tree[rightChild])

    def query(self, qLow, qHigh):
        return self.queryHelper(qLow, qHigh, 0, self.n-1, 0)

    def queryHelper(self, qLow, qHigh, low, high, pos):
        if qLow <= low and high <= qHigh:
            return self.tree[pos]
        if qHigh < low or qLow > high:
            return float("inf")

        mid = (low + high) // 2
        return min(self.queryHelper(qLow, qHigh, low, mid, 2*pos+1), \
            self.queryHelper(qLow, qHigh, mid+1, high, 2*pos+2))




segmentTree = SegmentTree([-1, 2, 4, 0, -3, 3, -4])
print(segmentTree.tree)
print(segmentTree.query(1,3))
print(segmentTree.query(0,3))
print(segmentTree.query(0,5))
print(segmentTree.query(3,6))
