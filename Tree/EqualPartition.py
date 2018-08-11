class Solution:
    def sumit(self, root, sums):
        if root:
            sums.append(self.sumit(root.left, sums) + self.sumit(root.right, sums) + root.val)

    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        sums = []
        self.sumit(root, sums)
        y = sums.pop()
        return y / 2 in sums
