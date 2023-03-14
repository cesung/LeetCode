from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return
        
        self.dfs(root.left)

        if self.prev != None:
            self.min_diff = min(
                self.min_diff,
                root.val - self.prev
            )
        self.prev = root.val

        self.dfs(root.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        INF = 10**5 + 1
        self.min_diff = INF
        
        self.dfs(root)

        return 0 if self.min_diff == INF else self.min_diff
