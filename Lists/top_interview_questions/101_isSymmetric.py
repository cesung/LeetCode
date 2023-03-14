# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, left_rt, right_rt):

        if left_rt.val != right_rt.val:
            return False

        if left_rt.left is None or right_rt.right is None:
            left_valid = (left_rt.left == right_rt.right)
        else:
            left_valid = self.dfs(left_rt.left, right_rt.right)

        if left_rt.right is None or right_rt.left is None:
            right_valid = (left_rt.right == right_rt.left)
        else:
            right_valid = self.dfs(left_rt.right, right_rt.left)

        return left_valid and right_valid

    # O(n) time | O(1) space
    def isSymmetric(self, root: TreeNode) -> bool:
        if root.left is None or root.right is None:
            return root.left == root.right

        return self.dfs(root.left, root.right)
