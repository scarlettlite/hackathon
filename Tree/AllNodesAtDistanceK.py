from collections import defaultdict, deque

class Solution:
    def creategraph(self, root, parent, graph):
        if root:
            graph[parent].append(root)
            graph[root].append(parent)
            self.creategraph(root.left, parent, graph)
            self.creategraph(root.right, parent, graph)

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = defaultdict(list)
        self.creategraph(root, None, graph)
        queue = deque([(target,0)])
        visited = set()
        ans = []
        while queue:
            node, d = queue.popleft()
            visited.add(node)
            if d > K:
                break
            if d == K:
                ans.append(node)
            if node:
                for v in graph[node]:
                    if v not in visited:
                        queue.append((v, d+1))

        return ans

