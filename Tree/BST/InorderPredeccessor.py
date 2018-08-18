class Solution:
    def maximum(self, root):
        curr = root
        while curr.right:
            curr = curr.right
        return curr

    def inorderPredeccessor(self, root, p, par):
        ans = None
        if root == p:
            if root.left:
                ans = self.maximum(root.left)
            elif par:
                ans = par
        else:
            if p.val < root.val:
                ans = self.inorderPredeccessor(root.left, p, par)
            else:
                ans = self.inorderPredeccessor(root.right, p, root)
        return ans

# Solution().inorderPredeccessor(roo)
