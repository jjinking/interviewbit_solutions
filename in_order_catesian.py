# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        return self._build_tree(A, 0, len(A) - 1)

    def _build_tree(self, A, start, end):
        if end < start:
            return None

        # First, find the maximum value and its position
        max_pos = start
        max_val = A[max_pos]
        for i in range(start + 1, end + 1):
            if max_val < A[i]:
                max_val = A[i]
                max_pos = i
        # print("start, end: {}, {}".format(start, end))
        # print("max_val, max_pos: {}, {}".format(max_val, max_pos))
        # Create new node at max value
        tn = TreeNode(max_val)

        # Build subtrees
        tn.left = self._build_tree(A, start, max_pos - 1)
        tn.right = self._build_tree(A, max_pos + 1, end)

        return tn

if __name__ == '__main__':
    Solution().buildTree([1, 2, 3])
