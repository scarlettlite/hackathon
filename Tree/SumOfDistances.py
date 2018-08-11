from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        tree = defaultdict(set)
        res = [0] * N
        count = [0] * N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root=0, seen=set()):
            seen.add(root)
            for i in tree[root]:
                if i not in seen:
                    dfs(i, seen)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]
            count[root] += 1

        def dfs2(root=0, seen=set()):
            seen.add(root)
            for i in tree[root]:
                if i not in seen:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, seen)
        dfs()
        dfs2()
        return res


print(Solution().sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))

