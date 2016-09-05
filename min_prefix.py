class Node(object):
    def __init__(self):
        self.children = {}
        self.freq = 0

    def add_child(self, char, child_node):
        self.children[char] = child_node

    def is_leaf(self):
        return len(self.children) == 0


class Solution:

    def __init__(self):
        self.root = Node()

    def get_prefix(self, word):
        curr_node = self.root
        running_c = []
        for c in word:
            running_c.append(c)
            curr_node = curr_node.children[c]
            if curr_node.freq <= 1:
                return ''.join(running_c)



    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        # Store word in tree
        for word in A:
            curr_node = self.root

            for c in word:
                curr_node.freq += 1
                if c not in curr_node.children:
                    curr_node.children[c] = Node()
                curr_node = curr_node.children[c]


        # Output the shorter representations
        result = [self.get_prefix(word) for word in A]
        return result


if __name__ == '__main__':
    print(Solution().prefix([ "zebra", "dog", "duck", "dot" ]) == ['z', 'dog', 'du', 'dot'])
    print(Solution().prefix([ "id", "qscdxrjmow", "rxsjybldbe", "sarcbyne", "dyggxxp", "lorel", "nmpa" ]) == ['i', 'q', 'r', 's', 'd', 'l', 'n'])
    print(Solution().prefix([ "bearcat", "bert" ]) == ['bea', 'ber'])
