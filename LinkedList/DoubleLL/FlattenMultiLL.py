"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list
"""
class Solution(object):
    def helper(self, node):
        head, tail, pointer = node, node, node
        while pointer:
            if pointer.child:
                childhead, childtail = self.helper(pointer.child)
                succ = pointer.next
                if succ:
                    succ.prev = childtail
                    childtail.next = succ
                pointer.next = childhead
                childhead.prev = pointer
                tail = childtail
                pointer = succ
            else:
                tail = pointer
                pointer = pointer.next
        

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        return self.helper(head)[0]
