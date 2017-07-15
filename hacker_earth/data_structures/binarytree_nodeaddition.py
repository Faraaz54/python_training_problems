from binary_tree import BinaryTree, preorder

class Binary(BinaryTree):
    def __init__(self, rootid=None):
        BinaryTree.__init__(self, rootid)
        self.rootid = rootid



t = Binary(1)
t.insertRight(2)
t.insertLeft(3)
t.insertLeft(5)

preorder(t)






