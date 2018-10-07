from collections import defaultdict
class Solution:
    def mstkruskals(self, edges,n):
        sets = defaultdict(set)
        for i in range(n):
            sets[i] = {i}
        edges.sort()
        final = set()
        for w,u,v in edges:
            if sets[u] != sets[v]:
                sets[u]|=sets[v]
                sets[v] = sets[u]
                final |= {(u,v)}
                if len(final) == n-1:
                    break
        return final

print(Solution().mstkruskals([[1,0,1],[2,1,3], [4,1,2]], 4))