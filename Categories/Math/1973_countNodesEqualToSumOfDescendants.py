from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root):
        left_sum = self.dfs(root.left) if root.left else 0
        right_sum = self.dfs(root.right) if root.right else 0

        if root.val == left_sum + right_sum:
            self.cnt += 1

        return (
            left_sum +
            right_sum +
            root.val
        ) 


    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        self.dfs(root)

        return self.cnt