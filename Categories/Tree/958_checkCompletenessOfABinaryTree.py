from typing import *
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        is_end = False

        while len(queue) > 0:
            node = queue.popleft()
            if node is not None:
                if is_end:
                    return False
                queue.append(node.left)
                queue.append(node.right)
            else:
                is_end = True

        return True