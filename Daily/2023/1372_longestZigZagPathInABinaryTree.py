from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # parent == -1, root
    # parent == 0, parent go left to root
    # parent == 1, right go right to root
    def dfs(self, root, parent):
        if root.left == None == root.right:
            return 1
        
        left_length = self.dfs(root.left, 0) if root.left is not None else 0
        right_length = self.dfs(root.right, 1) if root.right is not None else 0

        self.max_length = max(
            self.max_length,
            left_length,
            right_length,
        )

        if parent == -1:
            return max(
                left_length,
                right_length
            )
        elif parent == 0: # parent go left to root
            return right_length + 1
        else: # parent == 1, parent go right to root
            return left_length + 1


    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if root.left == None == root.right:
            return 0

        self.max_length = 0
        rst = self.dfs(root, -1)

        self.max_length = max(
            self.max_length,
            rst,
        )

        return self.max_length