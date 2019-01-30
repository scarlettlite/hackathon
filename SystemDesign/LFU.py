from collections import defaultdict, OrderedDict
class Node:
    def __init__(self, value):
        self.value = value
        self.freq = 1

class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.nodeDict = {}
        self.capacity = capacity
        self.freqDict = defaultdict(OrderedDict)
        self.minFreq = 0
        
    
    def increaseFrequency(self, key):
        node = self.nodeDict[key]
        #increment the frequency
        oldFreq = node.freq
        node.freq += 1

        #delete the node from previous frequency
        del self.freqDict[oldFreq][key]

        #if this was the only node in minimum frequency then update the minFreq
        if len(self.freqDict[oldFreq]) == 0 and self.minFreq == oldFreq:
            self.minFreq = node.freq 

        #put the node in the new frequency
        self.freqDict[node.freq][key] = node
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.nodeDict:
            return -1
        else:
            self.increaseFrequency(key)
            return self.nodeDict[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return 
        if key in self.nodeDict:
            self.increaseFrequency(key)
            self.nodeDict[key].value = value
        else:
            if self.capacity == len(self.nodeDict):
                """remove the minFreq key
                if there are more than one keys with minFreq then remove the least recently
                uses . 
                if there is only one key then with minFreq then remove that key and update                     minFreq
                there is no need update minFreq, when we insert a new element minFreq will                     become 1
                """
                ekey, enode = self.freqDict[self.minFreq].popitem(False)
                del self.nodeDict[ekey]
            
            node = Node(key)
            self.nodeDict[key] = node
            self.freqDict[1][key] = node
            self.minFreq = 1

lfu = LFUCache(2)
lfu.put(1,1)
lfu.put(2,2)
lfu.get(1)
lfu.put(3,3)
lfu.get(2)
lfu.get(3)
lfu.put(4,4)
lfu.get(1)
lfu.get(3)
lfu.get(4)