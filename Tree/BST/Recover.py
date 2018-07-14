"""
https://leetcode.com/problems/recover-binary-search-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self, root):
        result = []
        if root:
            result.extend(self.inorder(root.left))
            result.append(root)
            result.extend(self.inorder(root.right))
        return result


    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        it = self.inorder(root)
        i,j = None, None
        """
        Once you have the inorder, track where the ascending order is 
        incorrect and swap those nodes
        """
        for k in range(1, len(it)):
            if it[k-1].val < it[k].val:
                continue
            elif i == None:
                i = k-1
            elif j == None:
                j = k
                break

        if j == None:
            temp = it[i].val
            it[i].val = it[i+1].val
            it[i+1].val = temp
        else:
            temp = it[i].val
            it[i].val = it[j].val
            it[j].val = temp

        



