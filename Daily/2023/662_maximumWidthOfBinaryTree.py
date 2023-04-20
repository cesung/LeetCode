from typing import *
from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        INF = float('inf')
        max_width = 0
        rcd = defaultdict(lambda : INF)
        queue = deque()

        queue.append([root, 0, 1])
        while queue:
            node, level, label = queue.popleft()
            if node.left is not None:
                queue.append([node.left, level + 1, 2 * label])
            if node.right is not None:
                queue.append([node.right, level + 1, 2 * label + 1])
            
            rcd[level] = min(
                rcd[level],
                label,
            )
        
            max_width = max(
                max_width,
                label - rcd[level] + 1
            )

        return max_width