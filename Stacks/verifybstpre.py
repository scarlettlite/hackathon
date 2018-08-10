class TreeNode:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None

class Solution:
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack, low = [], float('-inf')
        for x in preorder:
            if x < low:
                return False
            if not stack:
                stack.append(x)
            else:
                if x < stack[-1]:
                    stack.append(x)
                else:
                    while stack and stack[-1] < x:
                        low = stack.pop()
                    stack.append(x)
        return True
        
# solution with O(1) space
# class Solution:
#     # use stack-pointer to reduce space to O(1)
#     def verifyPreorder(self, preorder):
#         """
#         :type preorder: List[int]
#         :rtype: bool
#         """
#         stack, low = -1, float('-inf')
#         for val in preorder:
#             if val < low:
#                 return False
#             while stack >= 0 and val > preorder[stack]:
#                 low = preorder[stack]
#                 stack -= 1
#             stack += 1
#             preorder[stack] = val
#         return True

print(Solution().verifyPreorder([5,2,6,1,3]))