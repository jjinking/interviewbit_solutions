class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal_count(self, A):
        s = [A]
        visited_count = {}
        result = []
        while s:
            n = s.pop()
            if n not in visited_count:
                visited_count[n] = 0
            visited_count[n] += 1
            if n.left is None and n.right is None:
                result.append(n.val)
            elif visited_count[n] == 2:
                result.append(n.val)
            else:
                if n.right is not None:
                    s.append(n.right)
                s.append(n)
                if n.left is not None:
                    s.append(n.left)
        return result

    def inorderTraversal(self, A):
        curr_node = A
        s = []
        result = []
        while s or curr_node is not None:
            # Keep going left until leaf
            if curr_node is not None:
                s.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = s.pop()
                result.append(curr_node.val)
                curr_node = curr_node.right
        return result
