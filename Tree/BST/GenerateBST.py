#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, nums):
        if not nums : return [None]
        ans = []
        if len(nums) == 1: 
            ans.append(TreeNode(nums[0]))
        else:
            for i,x in enumerate(nums):
                leftsubtrees = self.helper(nums[:i])
                rightsubtrees = self.helper(nums[i+1:])
                for left in leftsubtrees:
                    for right in rightsubtrees:
                        node = TreeNode(x)
                        node.left = left
                        node.right = right
                        ans.append(node)
        return ans
        
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper([i+1 for i in range(n)])

Solution().generateTrees(3)