class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder: return False
        preorder = preorder.split(',')[::-1]
        stack = [preorder.pop()]
        while stack:
            node = stack.pop()
            left, right = None, None
            if len(preorder) < 2: return False
            if preorder : left = preorder.pop() 
            if preorder : right = preorder.pop()
            if right != '#' and right != None: stack.append(right)
            if left != '#' and left != None: stack.append(left)
        if not stack and preorder: return False
        return True

print(Solution().isValidSerialization("1"))