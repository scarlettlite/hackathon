# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def encode(self, root):
        binary = None
        if root:
            binary = TreeNode(root.val)
            if root.children:
                node = TreeNode(root.children[0])
                binary.left = node
                for child in root.children[1:]:
                    node.right = self.encode(child)
                    node = node.right
        return binary

    def decode(self, data):
        nary = None
        if data:
            nary = Node(data.val, [])
            node = data.left
            while node:
                nary.children.append(self.decode(node))
                node = node.right
        return nary
        

def createnarytree():
    curr = root = Node(1, [])
    children = []
    for x in range(2, 14, 3):
        cdc = []
        for y in range(x, x+3):
            node = Node(y, [])
            cdc.append(node)
            if 2 <= y <= 4:
                children.append(node)
        curr.children = cdc
        curr = None if not children else children.pop(0)
    return root

nary = createnarytree()
c = Codec()
binary = c.encode(nary)
nnary = c.decode(binary)
