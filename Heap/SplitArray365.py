import heapq
from collections import defaultdict
class Sequence:
    def __init__(self, tail, size):
        self.tail = tail
        self.size = size

    def __lt__(self, other):
        if self.tail == other.tail:
            return self.size < other.size
        else:
            return self.tail > other.tail

class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tails = defaultdict(int)
        tails[nums[0]] = 1
        for x in nums[1:]:
            seq = heap[0]
            if seq.tail == x-1:
                tails[seq.tail] -= 1
                seq.tail = x
                seq.size += 1
                heapq.heappushpop(heap, seq)
                tails[seq.tail] += 1
            elif tails[x-1] > 0:
                    tails[x-1] -= 1
                    tails[x] += 1
            else:
                heapq.heappush(heap, Sequence(x,1))
                tails[x] += 1
       
        return all([True if seq.size > 2 else False for seq in heap])

print(Solution().isPossible([1,2,3,4,6,7,8,9,10,11]))