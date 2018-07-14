class Solution:
    def prefixSum(self, path):
        n = len(path)
        csum = []
        temp = 0
        for x in path:
            temp += x
            csum.append(temp)
        count = 0
        for i in range(n):
            for j in range(i,n):
                rsum = 0
                if i == 0:
                    rsum = csum[j]
                else:
                    rsum = csum[j] - csum[i-1]
                if rsum == inp:
                    count +=1
        return count

    def preorder(self, root, path):
        if not root : return 0
        path.append(root.val)
        if not root.left and not root.right:
            return self.prefixSum(path)
        ans = 0
        ans += self.preorder(root.left, path)
        ans += self.preorder(root.right, path)
        path.pop()
        return ans
        
    def pathSum(self, root, inp):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.preorder(root, [])
    
            



    