class Solution:
    def __init__(self):
        self.ans = set()

    def helper(self, candidates, target, solution):
        if target == 0:
            self.ans.add(tuple(solution[:]))
        else:
            for i,x in enumerate(candidates):
                if x <= target:
                    solution.append(x)
                    self.helper(candidates[i+1:], target-x, solution)
                    solution.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.helper(candidates, target, [])
        return [list(x) for x in self.ans]