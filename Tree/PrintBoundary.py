class Solution(object):
    def preorder(self, root):
        ans = []
        if root:
            if not root.left and not root.right:
                ans.append(root.val)
            else:
                ans.extend(self.preorder(root.left))
                ans.extend(self.preorder(root.right))
        return ans
    
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        s1, s2 = [], []
        s3 = self.preorder(root.left)
        s3.extend(self.preorder(root.right))
        curr = root.left
        while curr:
            if curr.left or curr.right:
                s1.append(curr.val)
            if curr.left :
                curr = curr.left
            else:
                curr = curr.right
                
        curr = root.right
        while curr:
            if curr.left or curr.right:
                s2.append(curr.val)
            if curr.right :
                curr = curr.right
            else:
                curr = curr.left
            
        return [root.val] + s1 + s3 + s2[::-1]