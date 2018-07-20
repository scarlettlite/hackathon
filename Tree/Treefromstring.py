class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getposition(self, s):
        c, o = 0,1
        i = 1
        while i < len(s) and o != 0:
            x = s[i]
            if x == '(':
                o+=1
            if x == ')':
                o-=1

            i+=1
        return i
    
    def helper(self, s):
        root = None
        if s:
            print(s)
            j = 0
            while j < len(s) and s[j] not in '()':
                j += 1
            root = TreeNode(int(s[:j]))
            i = self.getposition(s[j:])
            root.left = self.helper(s[j+1:j+i-1])
            root.right = self.helper(s[j+i+1:-1])
        return root
            
        
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        return self.helper(s)

param  = Solution().str2tree("-4(2(7893)(1))(6(5)(7))")
print(param.val)