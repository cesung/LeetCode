from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, node):
        if not node:
            return 0

        if node.left == None == node.right:
            return 1

        return max(
            self.dfs(node.left),
            self.dfs(node.right)
        ) + 1
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)