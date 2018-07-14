class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            """
            Main thing to remember here is
            push right first, so that the latest left child is at the top
            """
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans

    def postorderTraversal(self, root):
         """
        :type root: TreeNode
        :rtype: List[int]
        """

        """
        For solving a question in post order iterative way
        create the post order first then process each node
        """
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        
        return ans[::-1]


    def postorderTraversalOneStack(self, root):
        stack = []
        curr = root
        ans = []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = root.left
            if stack and stack[-1].right != None:
                curr = stack[-1].right
            else:
                node = stack.pop()
                ans.append(node.val)
                if stack and node == stack[-1].left and  stack[-1].right:
                    curr = stack[-1].right
        return ans

    def inorder(self, root):
        stack = []
        curr = root
        ans = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                curr = node.right

        return ans
            

                    
