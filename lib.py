import sys
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def read_tree(s):
    '''Read a tree from a string of input
    -1's indicate null/None nodes

    example: `t = lib.read_tree('1 2 3 -1 -1 4 -1 -1 5 -1 -1')`
    '''
    a = list(map(int, s.split()))
    len_a = len(a)
    root = TreeNode(a[0])
    q = Queue()
    q.put(root)
    i = 1
    while not q.empty():
        p = q.get()
        n_left = None
        if i < len_a and a[i] != -1:
            n_left = TreeNode(a[i])

        n_right = None
        if i < len_a and a[i + 1] != -1:
            n_right = TreeNode(a[i+1])

        p.left = n_left
        p.right = n_right
        if p.left is not None:
            q.put(p.left)
        if p.right is not None:
            q.put(p.right)
        i += 2

    return root


def preorder(root):
    if root is None:
        return []
    results = [root.val]
    results.extend(preorder(root.left))
    results.extend(preorder(root.right))
    return results


def postorder(root):
    if root is None:
        return []
    results = []
    results.extend(preorder(root.left))
    results.extend(preorder(root.right))
    results.append(root.val)
    return results


def inorder(root):
    if root is None:
        return []
    results = []
    results.extend(preorder(root.left))
    results.append(root.val)
    results.extend(preorder(root.right))
    return results


def get_depth(root):
    '''Get the maximum depth of a graph
    '''
    if root is None:
        return 0
    return 1 + max(get_depth(root.left), get_depth(root.right))


def print_tree(root):
    '''    1
         /   \
       2       4
      / \     / \
     x   3   x   5
    / \ / \ / \ / \
    x x x x x x x 6

    7 (2 ** 3 - 1)
    3 (2 ** 2 - 1)
    1 (2 ** 1 - 1)
    (2 ** (depth - i)) - 1
    '''
    depth = get_depth(root)
    q = Queue()
    q.put(root)
    for i in range(depth):
        # Compute spaces in between nodes
        n_spaces = (2 ** (depth - i)) - 1
        spaces = ' ' * n_spaces
        # Print padding
        left_pad = (2 ** (depth - i - 1)) - 1
        sys.stdout.write(' ' * (left_pad))
        # Get items to print for current row
        row_nodes = (q.get() for j in range(2 ** i))
        # Print node values
        for tn in row_nodes:
            if tn is not None:
                sys.stdout.write(str(tn.val) + spaces)
                q.put(tn.left)
                q.put(tn.right)
            else:
                sys.stdout.write('x' + spaces)
                q.put(None)
                q.put(None)
        sys.stdout.write('\n')


def flip(A):
    if A is None:
        return A
    if A.left is not None:
        A.left = flip(A.left)
    if A.right is not None:
        A.right = flip(A.right)
    A.left, A.right = A.right, A.left
    return A


def is_equal(r1, r2):
    if r1 is None and r2 is None:
        return True
    elif r1 is None:
        return False
    elif r2 is None:
        return False
    elif r1.val != r2.val:
        return False
    return is_equal(r1.left, r2.left) and is_equal(r1.right, r2.right)


def is_mirror_equal(r1, r2):
    '''Check if r1 is a mirror of r2
    '''
    if r1 is None and r2 is None:
        return True
    elif r1 is None:
        return False
    elif r2 is None:
        return False
    elif r1.val != r2.val:
        return False
    return is_mirror_equal(r1.left, r2.right) and \
        is_mirror_equal(r1.right, r2.left)
