import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.dict = {}

    def minheapify(self, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < len(self.heap) and self.heap[l] < self.heap[i]:
            largest = l
        if r < len(self.heap) and self.heap[r] < self.heap[i]:
            largest = r
        if largest != i:
            """
            you could swap in a function
            """
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.dict[self.heap[largest]] = largest
            self.dict[self.heap[i]] = i
            self.minheapify(largest)


    def getmin(self):
        return self.heap[0]

    def extractmin(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.dict[self.heap[0]] = 0
        self.dict[self.heap[-1]] = len(self.heap) - 1
        rv = self.heap.pop()
        del self.dict[rv]
        self.minheapify(0);
        return rv

    def insert(self, obj):
        self.increasekey(float('inf'), obj)

    def increasekey(self, oldkey, newkey):
        if oldkey != newkey:
            i = self.dict.get(oldkey)
            if i != None:
                i = self.dict[oldkey]
                del self.dict[oldkey]
                self.heap[i] = newkey
            else:
                self.heap.append(newkey)
                i = len(self.heap) - 1
            self.dict[newkey] = i
            if oldkey < newkey:
                self.minheapify(i)
            elif oldkey > newkey:
                p = i//2
                while i > -1 and self.heap[i] < self.heap[p]:
                    self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                    self.dict[self.heap[i]] = i
                    self.dict[self.heap[p]] = p
                    i, p = p, p//2


pq = PriorityQueue()
pq.insert(9)
pq.insert(8)
pq.insert(7)
pq.insert(6)
pq.insert(5)
pq.insert(4)

pq.increasekey(4,10)
pq.increasekey(9,2)

print(pq.extractmin())
print(pq.extractmin())
            