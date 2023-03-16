from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, preorder, inorder):
        size = len(preorder)
        if size == 0:
            return None
        
        root_val = preorder[0]
        root_idx = inorder.index(root_val)

        root = TreeNode(root_val)
        root.left = self.dfs(preorder[1:1+root_idx], inorder[:root_idx]) 
        root.right = self.dfs(preorder[root_idx+1:], inorder[root_idx+1:])

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(preorder, inorder)
        