"""
https://leetcode.com/problems/find-duplicate-subtrees
"""
from collections import defaultdict
class Solution:
    def preorder(self, root, tt):
        pre = ""
        if root:
            pre = '#' + str(root.val)
            pre += '(' + self.preorder(root.left, tt) + ')' + '(' + self.preorder(root.left, tt) + ')'
            tt[pre].append(root)
        return pre

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        tt = defaultdict(list)
        self.preorder(root, tt)
        ans = []
        for key, value in tt.items():
            if len(value) > 1:
                ans.append(value[0])
        return ans
