class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []
        
class Solution:
    def getkills(self, root):
        if root == None: return 0
        kills = 1
        for child in root.children:
            kills += self.getkills(child)
        return kills
    
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        root = None
        treedict = {}
        for p in pid:
            treedict[p] = TreeNode(p)
        for i,p in enumerate(ppid):
            if p == 0:
                root = treedict[pid[i]]
            else:
                treedict[p].children.append(treedict[pid[i]])
        return self.getkills(treedict[kill])

print(Solution().killProcess([1,3,10,5],
[3,0,5,3],
5))