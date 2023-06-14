from typing import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_traversal(self, root):
        if root.left is not None:
            self.inorder_traversal(root.left)
        
        if self.prev != -1:
            self.min_diff = min(
                self.min_diff,
                abs(root.val - self.prev)
            )
        self.prev = root.val

        if root.right is not None:
            self.inorder_traversal(root.right)
            

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        INF = float('inf')
        self.min_diff = INF
        self.prev = -1

        self.inorder_traversal(root)

        return self.min_diff
        