from collections import deque
"""
link to leetcode problem goes here:
"""
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

class Solution:
    def serializetree(self, nums):
        tree = [None for _ in range(15)]
        for num in nums:
            level = num//100
            position = (num%100) //10
            value = num%10
            index = (2**(level-1) - 1) + (position-1)
            #print(level, position, value)
            tree[index] = value     
        return tree
    
    def deserializetree(self, tree):
        if not tree : return None
        
        return root
                        
    def pathsums(self, root, path, psum):
        if root == None : return 
        path.append(root.val)
        print(path)
        if not root.left and not root.right:
            psum[0] += sum(path)
        else:
            self.pathsums(root.left, path, psum)
            self.pathsums(root.right, path, psum)
        path.pop()
        
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tree = self.serializetree(nums)
        print(tree)
        root = self.deserializetree(tree)
        ans = [0]
        self.pathsums(root, [], ans)
        return ans[0]
        

print(Solution().pathSum([113,229,330,466]))