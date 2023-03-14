# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root):

        if root.left is None and root.right is None:
            return 1

        depth_left, depth_right = 0, 0

        if root.left is not None:
            depth_left = self.dfs(root.left)

        if root.right is not None:
            depth_right = self.dfs(root.right)

        return 1 + max(depth_left, depth_right)

    # O(n) time | O(1) space
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if root is None else self.dfs(root)
