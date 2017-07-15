class BinaryTree(object):
    def __init__(self, rootid=None):
        self.left = None
        self.right = None
        self.rootid = rootid
        self.parents = [rootid]


    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self, value):
        self.rootid = value

    def getNodeValue(self):
        return self.rootid

    def insert(self, newNode,parent):
        if parent in self.parents:
            Tree = BinaryTree(parent)
            if Tree.right is None:
                Tree.right = BinaryTree(newNode)
            else:
                Tree.left = BinaryTree(newNode)
        else:
            Tree = BinaryTree(parent)
            self.parents.append(parent)

    def insertLeft(self, newNode):
        if self.left is None:
            self.left = BinaryTree(newNode)
        else:
            Tree = BinaryTree(newNode)
            Tree.left = self.left
            self.left = Tree

def preorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        print(tree.getNodeValue())
        preorder(tree.getRightChild())


b = BinaryTree(0)

b.insert(1,0)
b.insert(3,2)

print b.getLeftChild()

preorder(b)