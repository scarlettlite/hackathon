class Solution:
    def getdepth(self, nestedList):
        depth = 0 if not nestedList else 1
        for x in nestedList:
            if not x.isInteger():
                depth = max(1+self.getdepth(x.getList()), depth)
        return depth
    
    def getsum(self, depth, nestedList):
        depthsum = 0
        for x in nestedList:
            if x.isInteger():
                depthsum += depth * x.getInteger()
            else:
                depthsum += self.getsum(depth-1, x.getList())
        return depthsum
         
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        depth = self.getdepth(nestedList)
        ans = self.getsum(depth, nestedList)
        return ans