from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, l_rt, r_rt):
        if not l_rt and not r_rt:
            return True
        if not l_rt or not r_rt:
            return False
        
        if l_rt.val != r_rt.val:
            return False
        
        return (
            self.dfs(l_rt.right, r_rt.left) & 
            self.dfs(r_rt.right, l_rt.left)
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)
        