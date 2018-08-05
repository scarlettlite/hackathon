"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        pointer, node = head, Node(insertVal, None)
        if not head:
            node.next = node
            head = node
        else:
            while pointer.val <= pointer.next.val:
                pointer = pointer.next
            largest, smallest = pointer, pointer.next
            prev = None
            if node.val <= smallest.val or node.val >= largest.val:
                prev = largest
            elif node.val < head.val:
                pointer = smallest
                while node.val > pointer.val:
                    prev = pointer
                    pointer = pointer.next
            elif node.val == head.val:
                prev = head
            else:
                pointer = head
                while node.val > pointer.val:
                    prev = pointer
                    pointer = pointer.next
            succ = prev.next
            prev.next = node
            node.next = succ
        
        return head

head = Node(3, None)
node = Node(4, None)
node1 =  Node(1, None)
node2 =  Node(2, None)
head.next = node
node.next = node1
node1.next = node2
node2.next = head


Solution().insert(head, 0)
# Solution().insert(head, 6)
# Solution().insert(head, 4)
# Solution().insert(head, 2.75)
pointer = head.next
print(head.val)
while pointer != head:
    print(pointer.val)
    pointer = pointer.next


