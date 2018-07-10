# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head):
            """
            :type head: RandomListNode
            :rtype: RandomListNode
            """
            if not head : return head
            curr = head
            while curr:
                node = RandomListNode(curr.val)
                node.next = curr.next
                curr.next = node
            curr = head 
            while curr:
                cp = curr.next
                if curr.random : cp.random = curr.random.next
                curr = cp.next

            curr = head
            copyhead = curr.next
            while curr:
                cp = curr.next
                curr.next = cp.next
                if curr.next : cp.next = curr.next.next
                curr = curr.next
            return copyhead