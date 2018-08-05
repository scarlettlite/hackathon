class Solution(object):
    def preorder(self, root):
        ans = ''
        if root:
            ans = str(root.val)
            ans += '(' + self.preorder(root.left) + ')'
            ans += '(' + self.preorder(root.right) + ')'

        return ans

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        p1 = self.preorder(s)
        p2 = self.preorder(t)
        if p1.find(p2) > -1:
            return True
        return False

        