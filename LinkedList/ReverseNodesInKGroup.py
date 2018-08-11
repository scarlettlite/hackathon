from random import uniform
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, head):
        if not head: return head
        prev, curr, succ = None, head, head.next
        while curr:
            curr.next = prev
            prev = curr
            curr = succ
            if succ: succ = succ.next
        return prev

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        it, i, prehead, prev = head, 0, ListNode(-1), None
        prehead.next = head
        while it:
            i = 0
            gh = it
            while it and i < k - 1:
                it = it.next
                i += 1
            if it: 
                temp = it.next
                it.next = None
                ngh = self.reverse(gh)
                if prev: prev.next = ngh
                gh.next = temp
                prev = gh
                if gh == head:
                    prehead.next = ngh
                i = 0
                it = temp
        return prehead.next

def printll(head):
    it = head
    while it:
        print(it.val, ' ', end='')
        it = it.next
    print()

head = ListNode(1)
pi = head
for i in range(10):
    pi.next = ListNode(uniform(1,20))
    pi = pi.next
printll(Solution().reverseKGroup(head,4))

            
