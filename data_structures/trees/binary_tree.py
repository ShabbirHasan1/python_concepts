import random
from collections import deque

class BinaryTreeNode:
    '''
    Binary Tree node that gets use to construct Binary Trees
    '''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None
        self.parent = None
        self.count = None


def insert(root, val):
    '''
    Insert a new code to the Binary Tree
    :param root: root of the binary tree : BinaryTreeNode
    :param val: data
    :return: root node: BinaryTreeNode
    '''
    new_node = BinaryTreeNode(val)
    if root is None:
        return new_node

    parent = None
    tmp_note = root
    while (tmp_note is not None):
        parent = tmp_note
        if val < tmp_note.data:
            tmp_note = tmp_note.left
        else:
            tmp_note = tmp_note.right

    if val < parent.data:
        parent.left = new_node
    else:
        parent.right = new_node
    return root

def find_in_bst(root, data):
    '''
    It finds the data in binary search trees
    :param root: BinaryTreeNode
    :param data: any
    :return: node : BinaryTreeNode
    '''
    if root is None:
        return None

    if root.data == data:
        return root
    elif root.data > data:
        return find_in_bst(root.left, data)
    else:
        return find_in_bst(root.right, data)



def find_node(root, data):
    '''
    find node in inorder
    :param root: root of the bst
    :param d: data
    :return: BinaryTreeNode
    '''
    if root is None:
        return

    if root.data == data:
        return root

    temp = find_node(root.left, data)
    if temp is not None:
        return temp

    return find_node(root.right, data)


def display_inorder(node):
    if node is None:
        return

    display_inorder(node.left)
    print(f'{node.data}  ')
    display_inorder(node.right)


def create_BST(arr):
    root = None
    for x in arr:
        root = insert(root, x)
    return root


def create_binary_tree(count):
    root = None
    for _ in range(1, count):
        root = insert(root, random.randrange(1, 100))
    return root


def create_random_BST(count):
    root = None
    for _ in range(1, count):
        root = insert(root, random.randrange(200, 300))
    return root


def bst_to_list_rec(root, lst):
    if root is None:
        return

    bst_to_list_rec(root.left, lst)
    lst.append(root.data)
    bst_to_list_rec(root.right, lst)


def bst_to_list(root):
    lst = []
    bst_to_list_rec(root, lst)
    return lst


def populate_parents_rec(root, parent):
    if root is None:
        return
    root.parent = parent

    populate_parents_rec(root.left, root)
    populate_parents_rec(root.right, root)


def populate_parents(root):
    populate_parents_rec(root, None)


def display_level_order(root):
    if root is None:
        return
    que = deque()
    que.append(root)

    while que:
        temp = que.popleft()
        print(f'{temp.data} ')
        if temp.left is not None:
            que.append(temp.left)
        if temp.right is not None:
            que.append(temp.right)


def get_level_order(root):
    output = []
    if root is None:
        return output

    que = deque()
    que.append(root)

    while que:
        temp = que.popleft()
        output.append(temp.data)
        if temp.left is not None:
            que.append(temp.left)
        if temp.right is not None:
            que.append(temp.right)
    return output


def get_inorder_helper(root, output):
    if root is None:
        return output

    output = get_inorder_helper(root.left, output)
    output.append(root.data)
    output = get_inorder_helper(root.right, output)

    return output


def get_inorder(root):
    output = []
    return get_inorder_helper(root, output)


def is_identical_tree(root1, root2):
    """
    Compare two binary tress using recursion
    :param root1: BinaryTreeNode
    :param root2: BinaryTreeNode
    :return: Boolean
    """
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None and root1.data == root2.data:
        return is_identical_tree(root1.left, root2.left) and is_identical_tree(root1.right, root2.right)

    return False