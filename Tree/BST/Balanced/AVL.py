import random
from math import log2
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def getheight(self, node):
        height = 0
        if node:
            height = node.height
        return height

    def balance(self, node, parent):
        lheight, rheight = self.getheight(node.left), self.getheight(node.right)
        left, right = node.left, node.right
        newnode = None
        if lheight > rheight:
            node.left = left.right
            left.right = node
            newnode = left
        else:
            node.right = right.left
            right.left = node
            newnode = right
        if not parent:
            self.root = newnode
        else:
            if parent.left == node:
                parent.left = newnode
            else:
                parent.right = newnode
        node.height = 1 + max(self.getheight(node.left), self.getheight(node.right))
        newnode.height = 1 + max(self.getheight(newnode.left), self.getheight(newnode.right))


    def recursivelyInsert(self, node, root, parent):
        if root:
            if node.val <= root.val:
                if root.left == None:
                    root.left = node
                else:
                    self.recursivelyInsert(node, root.left, root)
            else:
                if root.right == None:
                    root.right = node
                else:
                    self.recursivelyInsert(node, root.right, root)
            if (abs(self.getheight(root.left) - self.getheight(root.right)) > 1):
                self.balance(root, parent)
            root.height = 1 + max(self.getheight(root.left), self.getheight(root.right))


    def insert(self, val):
        node = TreeNode(val)
        if self.root == None:
            self.root = node
        else:
            self.recursivelyInsert(node, self.root, None)


def main():
    avl = AVLTree()
    for i in range(1, 100000):
        rn = random.randint(1,100000)
        avl.insert(rn)
        height = avl.getheight(avl.root)
        logi = log2(i)
        if abs(height - logi) > 1 :
            print(height, logi)
            
    print()

main()









