from collections import deque
class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        self.buildmaxheap()

    def maxheapify(self, i):
        l = 2*i + 1
        r = 2*(i+1)
        largest = i
        if l < self.size and self.arr[l] > self.arr[largest]:
            largest = l
        if r < self.size and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.maxheapify(largest)

    def insert(self, key):
        self.arr.append(key)
        self.size +=1
        self.arr[self.size - 1], self.arr[0] = self.arr[0],self.arr[self.size - 1]
        self.maxheapify(0)


    def buildmaxheap(self):
        self.size = len(self.arr)
        n = self.size // 2
        for i in range(n, -1,-1):
            self.maxheapify(i)

    def extractmax(self):
        self.arr[self.size - 1], self.arr[0] = self.arr[0],self.arr[self.size - 1]
        mv = self.arr.pop()
        self.size -= 1
        return mv

    def heapsort(self):
        for i in range(self.size-1):
            self.arr[self.size - 1], self.arr[0] = self.arr[0],self.arr[self.size - 1]
            self.size -= 1
            self.maxheapify(0)


heap = Heap([2,5,6,3,1,7])

heap.heapsort()
print(heap.arr)
heap.buildmaxheap()
print(heap.arr)

        