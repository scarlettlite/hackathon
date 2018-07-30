from collections import defaultdict
class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        m = defaultdict(list)
        for i,x in enumerate(B):
            m[x].append(i)
        ans = []
        for x in A:
            ans.append(m[x].pop())
        return ans
        