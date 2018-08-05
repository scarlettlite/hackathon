"""
The idea here is to create a graph from a tree and then do a BFS on the 
given node
"""
from collections import defaultdict, deque
class Solution:
    def creategraph(self, root, parent, graph):
        if parent and root:
            graph[parent.val].append(root)
            graph[root.val].append(parent)
            self.creategraph(root.left, root, graph)
            self.creategraph(root.right, root.right, graph)

    def getclosest(self, k, graph):
        dist = {}
        queue = deque([k])
        visited = set()
        while queue:
            n = queue.popleft()
            if not root.left and not root.right:
                return n
            visited.add(n.val)
            for v in graph[n.val]:
                if v not in visited:
                    queue.append(v)
        


    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        self.creategraph(root, None, graph)

        return self.getclosest(k, graph)
        