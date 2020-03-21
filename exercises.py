def BinaryTreeList(root):
    return [root, [], []]


def insert_left(root):
    sub_tree = sub_tree


def insert_right(root):
    pass


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.left = None
        self.right = None

    def __repr__(self):
        return f"[[ Root: {self.root}. LChild:[{self.left}]. RChild:[{self.right}] ]]"

    def insert_left(self, root):
        new_tree = BinaryTree(root)
        if self.left:
            new_tree.left = self.left
            self.left = new_tree
        else:
            self.left = new_tree

    def insert_right(self, root):
        new_tree = BinaryTree(root)
        if self.right:
            new_tree.right = self.right
            self.right = new_tree
        else:
            self.right = new_tree

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_root_val(self, value):
        self.root = value
        return self.root

    def get_root_val(self):
        return self.root


def preorder(node): #nlr
    pass


def postorder(): #lrn
    pass


def inorder(): #lnr
    pass


def is_unival_tree(root):
    if not root:
        return True
    seen = set()



def invert():
    pass


def second_minimum_node():
    pass
