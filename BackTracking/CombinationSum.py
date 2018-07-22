class Solution:
    def __init__(self):
        self.ans = []
        
    def helper(self, solution, target, candidates):
        if target == 0:
            self.ans.append(solution[:])
        else:
            for j,x in enumerate(candidates):
                if x <= target:
                    solution.append(x)
                    self.helper(solution, target-x, candidates[j:])
                    solution.pop()
        
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.helper([], target, candidates)
        return self.ans

print(Solution().combinationSum([2,3,5], 8))