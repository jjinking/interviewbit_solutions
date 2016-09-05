#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BTreeBuilder:
    def __init__(self):
        self.root = None

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)
        # if node is None:
        #     node = TreeNode(val)
        # elif val < self.node.val:
        #     self._insert(node.left)
        # else:
        #     self._insert(node.right)

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _print(self, node):
        if node.left is not None:
            self._print(node.left)
        print(node.val)
        if node.right is not None:
            self._print(node.right)

    def print(self):
        self._print(self.root)


class Solution:

    # @param root : root node of tree
    # @param k : integer
    # @return an integer
    def kthsmallest(self, root, k):
        resultl = [None]
        try:
            self._kthsmallest(root, [k], resultl)
        except ValueError:
            return resultl[0]

    def _kthsmallest(self, root, kl, resultl):
        if root.left is not None:
            self._kthsmallest(root.left, kl, resultl)

        kl[0] -= 1
        # print("val: ", root.val)
        # print("k: ", k)
        if kl[0] == 0:
            resultl[0] = root.val
            raise ValueError

        if root.right is not None:
            self._kthsmallest(root.right, kl, resultl)

    # def kthsmallest3(self, root, k):
    #     node = root
    #     stack = [node]
    #     seen = set()
    #     while stack:
    #         print([nd.val for nd in stack])
    #         node = stack.pop()
    #
    #         if node.right is not None and node not in seen:
    #             stack.append(node.right)
    #
    #         if node.left is None:
    #             k -= 1
    #             print("Node, k: ", node.val, k)
    #             if k == 0:
    #                 return node.val
    #         elif node not in seen:
    #             stack.append(node)
    #             stack.append(node.left)
    #         seen.add(node)


if __name__ == '__main__':
    tb = BTreeBuilder()
    tb.insert(7)
    tb.insert(2)
    tb.insert(1)
    tb.insert(3)
    print("Graph---")
    tb.print()
    print("--------")
    s = Solution()
    print("solution:", s.kthsmallest(tb.root, 2))
