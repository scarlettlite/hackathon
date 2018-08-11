from random import choice
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small, big = ListNode(-1), ListNode(-1)
        it1, it2, it = small, big, head
        while it:
            if it.val < x:
                it1.next = it
                it1 = it1.next
            else:
                it2.next = it
                it2 = it2.next
            temp = it.next
            it.next = None
            it = temp
        it1.next = big.next
        return small.next

def printll(head):
    it = head
    while it:
        print(it.val, ' ', end='')
        it = it.next
    print()

head = ListNode(1)
pi = head
for i in range(10):
    pi.next = ListNode(choice(range(20)))
    pi = pi.next
printll(head)
printll(Solution().partition(head,10))
        