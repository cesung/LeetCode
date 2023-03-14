# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.cnt = 0
        self.tar = 0

    def inorder_traversal(self, root, k):
        # left subtree
        if root.left is not None:
            self.inorder_traversal(root.left, k)

        self.cnt += 1
        if self.cnt == k:
            self.tar = root.val

        # right subtree
        if root.right is not None:
            self.inorder_traversal(root.right, k)

    # O(n) time | O(1) space
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorder_traversal(root, k)

        return self.tar
