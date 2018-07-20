class Solution:

    def helper(self, arr):
        ans = True
        if arr:
            root = arr[0]
            bigger = -1
            for i,x in enumerate(arr):
                if x < root and bigger != -1:
                    ans = False
                    break
                if x > root and bigger == -1:
                    bigger = i
            if ans and bigger > 0:
                ans = self.helper(arr[1: bigger]) and self.helper(arr[bigger:])
            if ans and bigger == -1:
                ans = self.helper(arr[1:])
        return ans
        
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        return self.helper(preorder)

Solution().verifyPreorder([4,2,3,1])