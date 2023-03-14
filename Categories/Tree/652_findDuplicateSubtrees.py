from typing import *
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return "#,"
        
        encoding = str(root.val) + ',' + self.dfs(root.left) + ',' + self.dfs(root.right)
        
        self.rcd[encoding] += 1
        if self.rcd[encoding] == 2:
            self.ret.append(root)

        return encoding

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.rcd = defaultdict(int)

        self.ret = []
        self.dfs(root)

        return self.ret
        