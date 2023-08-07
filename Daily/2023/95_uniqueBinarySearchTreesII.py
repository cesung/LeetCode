from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, left: int, right: int) -> List[Optional[TreeNode]]:
        if left > right:
            return [None]
        elif left == right:
            return [TreeNode(val = left + 1)]
        
        roots = []
        for idx in range(left, right + 1):
            left_trees = self.dfs(left, idx - 1)
            right_trees = self.dfs(idx + 1, right)
            
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(
                        val = idx + 1, 
                        left = left_tree, 
                        right = right_tree
                    )
                    roots.append(root)
        
        return roots

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.dfs(0, n - 1)