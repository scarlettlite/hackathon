class Solution:
    def minimun(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr

    def deleteNodeHelper(self, root, key, par):
        if root:
            if root.val == key:
                if root.left and root.right:
                    minnode = self.minimun(root.right)
                    root.val, minnode.val = minnode.val, root.val
                    self.deleteNodeHelper(root.right, minnode.val, root)
                else:
                    if par:
                        child = root.right or root.left
                        if par.left == root:
                            par.left = child
                        else:
                            par.right = child
                    else:
                        root =  root.right or root.left
            else:
                if root.val < key:
                    self.deleteNodeHelper(root.right, key, root)
                else:
                    self.deleteNodeHelper(root.left, key, root)
        return root

    def deleteNode(self, root, key):  
        return self.deleteNodeHelper(root, key, None)