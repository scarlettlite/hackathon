"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def helper(self, root):
        head, tail = root, root
        if root:
            lefthead, lefttail = self.helper(root.left)
            righthead, righttail = self.helper(root.right)
            if lefttail:
                lefttail.right = root
                root.left = lefttail
                head = lefthead
            
            if righthead:
                righthead.left = root
                root.right = righthead
                tail = righttail
        
        return head, tail

    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        head, tail = self.helper(root)
        if head and tail:
            head.left = tail
            tail.right = head
        return head
