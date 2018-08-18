class Solution(object):
    def minimum(self, root):
        ans = None
        if root:
            curr = root
            while curr.left:
                curr = curr.left
            ans = curr
        return ans
    
    def getio(self, root, p, path):
        ans = None
        if root == p:
            """
            if the root has a right child, then its inorder 
            succesor is the minimum node in its right 
            subtree
            """
            if root.right:
                ans = self.minimum(root.right)
            elif path:
                """
                if root doesnt have a right subtree then, its inorder
                successor is the last ancestor greater than itself. if an
                ancestor is greater than its children then we can reach its
                smaller children by going to its left subtree. So every time
                we take a left turn from an ancestor save it in a cache
                """
                ans = path[-1]
        else:
            if p.val < root.val:
                """
                we can just save the last node. No need to store all ancestors 
                """
                path.append(root)
                ans = self.getio(root.left, p, path)
            else:
                ans = self.getio(root.right, p, path)
        return ans
                    
            
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        return self.getio(root, p, [])