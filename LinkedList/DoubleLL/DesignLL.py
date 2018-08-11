class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        i, it = 0, self.head
        while it and i < index:
            it = it.next
            i += 1
        if not it:
            return -1
        else:
            return it.val
        
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if self.head:
            self.head.prev = node
        node.next = self.head
        self.head = node
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        it = self.head
        while it and it.next:
            it = it.next
        node = Node(val)
        it.next = node
        node.prev = it
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == 0:
            self.addAtHead(val)
            return

        i, it, node = 0, self.head, Node(val)
        while it and i < index:
            i += 1
            it = it.next
        node.next = it
        if it == None and i == index:
            self.addAtTail(val)
        if it:
            node.prev = it.prev
            it.prev = node
            node.prev.next = node
        
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        i, it = 0, self.head
        while it and i < index:
            i += 1
            it = it.next
        if it:
            if it == self.head:
                node = self.head
                self.head = node.next
                node.next = None
            else:
                if it.prev : it.prev.next = it.next
                if it.next : it.next.prev = it.prev
                it.prev, it.next = None, None

    def printll(self):
        it = self.head
        while it:
            print(it.val,'->', end='')
            it = it.next
        print('')


ll = MyLinkedList()
ll.addAtHead(1)
ll.addAtIndex(1,2)
ll.get(1)
ll.get(0)
ll.get(2)
ll.printll()
