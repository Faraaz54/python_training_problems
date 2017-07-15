class BinaryTree(object):
    def __init__(self, rootid=None):
        self.left = None
        self.right = None
        self.rootid = rootid

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self, value):
        self.rootid = value

    def getNodeValue(self):
        return self.rootid

    def insertRight(self, newNode):
        if self.right is None:
            self.right = BinaryTree(newNode)
        else:
            Tree = BinaryTree(newNode)
            Tree.right = self.right
            self.right = Tree

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
def inorder(tree):
    if tree:
        preorder(tree.getRightChild())
        print(tree.getNodeValue())
        preorder(tree.getLeftChild())


'''class Tree:
    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None
        self.node_paths = {}
    
    def insert_left(self, value, parent):
        tree = Tree(value)
        if parent == 1:
            self.left = tree
            self.node_paths[value] = "L"
        else:
            temp = self
            self.node_paths[value] = ""
            for path in self.node_paths[parent]:
                if path == "L":
                    temp = temp.get_left_node()
                    self.node_paths[value] += "L"
                else:
                    temp = temp.get_right_node()
                    self.node_paths[value] += "R"
            temp.left = tree
            self.node_paths[value] += "L"
 
    def insert_right(self, value, parent):
        tree = Tree(value)
        if parent == 1:
            self.right = tree
            self.node_paths[value] = "R"
        else:
            temp = self
            self.node_paths[value] = ""
            for path in self.node_paths[parent]:
                if path == "L":
                    temp = temp.get_left_node()
                    self.node_paths[value] += "L"
                else:
                    temp = temp.get_right_node()
                    self.node_paths[value] += "R"
            temp.right = tree
            self.node_paths[value] += "R"
 
    def get_node_from_path(self, required_path):
        for node, path in self.node_paths.items():
            if path == required_path:
                return node
        return -1
 
    def get_node_path(self, value):
        return self.node_paths[value]
    
    def get_left_node(self):
        return self.left
    
    def get_right_node(self):
        return self.right
            
def print_tree(tree):
    if not tree:
        print "L", print_tree(tree.get_left_node())
        print "Value: ", tree.value
        print "R", print_tree(tree.get_right_node())
    
tree = Tree(1)
n, q = map(int, raw_input().strip().split())
# n = 10
# q = 8
# a = [
#     [1, 2, 'R'],
#     [1, 3, 'L'],
#     [2, 4, 'R'],
#     [2, 5, 'L'],
#     [3, 6, 'R'],
#     [3, 7, 'L'],
#     [5, 8, 'R'],
#     [5, 9, 'L'],
#     [7, 10, 'R']
# ]
 
for i in range(n - 1):
    parent, child, path = raw_input().strip().split()
    parent = int(parent)
    child = int(child)
    # parent, child, path = a[i]
    if path == "L":
        tree.insert_left(child, parent)
    else:
        tree.insert_right(child, parent)
# q = [2,
# 5,
# 3,
# 6,
# 1,
# 10,
# 9,
# 4]
 
# print "Paths: ", tree.node_paths
 
for i in range(q):
    question = int(raw_input())
    if question == 1:
        print 1
        continue
    path = tree.get_node_path(question)
    q_rev = ""
    for p in path:
        if p == "L":
            q_rev += "R"
        else:
            q_rev += "L"
    print tree.get_node_from_path(q_rev)
'''
















