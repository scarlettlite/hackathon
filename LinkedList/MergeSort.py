from random import choice
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def divide(self, head):
        head1, head2 = None, None
        if head:
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            head2 = slow.next
            slow.next = None
            head1 = head
        return head1, head2
    
    def merge(self, head1, head2):
        mergedList = ListNode(-1)
        mergedListIt = mergedList
        while head1 and head2:
            if head1.val < head2.val:
                mergedListIt.next = head1
                head1 = head1.next
            else:
                mergedListIt.next = head2
                head2 = head2.next
            mergedListIt = mergedListIt.next
        if head1:
            mergedListIt.next = head1
        elif head2:
            mergedListIt.next = head2
        return mergedList.next
            
    def mergeSort(self, head):
        sortedList = head
        if head and head.next :
            head1, head2 = self.divide(head)
            head1 = self.mergeSort(head1)
            head2 = self.mergeSort(head2)
            sortedList = self.merge(head1, head2)
        return sortedList
            
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.mergeSort(head)

def printll(head):
    it = head
    while it:
        print(it.val, ' ', end='')
        it = it.next
    print()

head = ListNode(1)
pi = head
for i in range(5):
    pi.next = ListNode(choice(range(1,20)))
    pi = pi.next

printll(Solution().sortList(head))