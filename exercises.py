def BinaryTreeList():
    pass


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f"[[ Root: {self.root}. LChild:[{self.left_child}]. RChild:[{self.right_child}] ]]"

    def insert_left(self, root):
        new_tree = BinaryTree(root)
        if self.left_child:
            new_tree.left_child = self.left_child
            self.left_child = new_tree
        else:
            self.left_child = new_tree

    def insert_right(self, root):
        new_tree = BinaryTree(root)
        if self.right_child:
            new_tree.right_child = self.right_child
            self.right_child = new_tree
        else:
            self.right_child = new_tree

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_val(self, value):
        self.root = value
        return self.root

    def get_root_val(self):
        return self.root


def preorder(node):
    pass


def postorder():
    pass


def inorder():
    pass


def is_unival_tree():
    pass


def invert():
    pass


def second_minimum_node():
    pass


# Quick tests
a = BinaryTree(5)
a.insert_left(4)
print(a)
