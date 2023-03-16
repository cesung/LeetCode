from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, inorder, postorder):
        size = len(inorder)
        if size == 0:
            return None
        root_val = postorder[-1]
        root_idx = inorder.index(root_val)
        right_size = size - (root_idx + 1)

        root = TreeNode(root_val)
        root.right = self.dfs(inorder[root_idx + 1:], postorder[-right_size-1:-1])
        root.left = self.dfs(inorder[:root_idx], postorder[-size:-right_size-1])

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(inorder, postorder)