# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

# Just implemented a BST ¯\_(ツ)_/¯


class Node:
    def __init__(self, data, l_child=None, r_child=None):
        self.data = data
        self.left = l_child
        self.right = r_child


def insert(root, node):
    if root is None:
        root.data = node
    else:

        if root.data > node.data:

            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)


def display(root):
    if root is None:
        return
    display(root.left)
    print(root.data)
    display(root.right)


head = Node(10)
insert(head, Node(6))
insert(head, Node(123))
insert(head, Node(321))
insert(head, Node(3))
insert(head, Node(13))
insert(head, Node(11))
insert(head, Node(12))

display(head)

# TODO:
# BST xD
