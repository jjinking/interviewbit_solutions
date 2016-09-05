# Definition for a  binary tree node
import lib


class Solution:

    def mirror_equal(self, r1, r2):
        if r1 is None and r2 is None:
            return True
        elif r1 is None:
            return False
        elif r2 is None:
            return False
        elif r1.val != r2.val:
            return False
        return self.mirror_equal(r1.left, r2.right) and self.mirror_equal(r1.right, r2.left)

    def isSymmetric(self, A):
        return self.mirror_equal(A.left, A.right)



if __name__ == '__main__':
    root = lib.TreeNode(2)
    root.left = lib.TreeNode(1)
    root.right = lib.TreeNode(3)

    print("inorder")
    print(Solution()._inorder(root))
    print("preorder")
    print(Solution()._preorder(root))
    print("postorder")
    print(Solution()._postorder(root))
