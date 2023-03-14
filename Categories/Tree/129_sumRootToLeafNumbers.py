from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, val):
        val *= 10
        val += root.val

        if root.left == None == root.right:
            self.ttl += val
            return

        if root.left:
            self.dfs(root.left, val)
        if root.right:
            self.dfs(root.right, val)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ttl = 0
        self.dfs(root, 0)

        return self.ttl