from typing import *
from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque() 
        rcd = defaultdict(list)
        queue.append( [root, 1] )

        while queue:
            root, level = queue.popleft()
            rcd[level].append(root.val)
            if root.left is not None:
                queue.append( [root.left, level + 1])
            if root.right is not None:
                queue.append( [root.right, level + 1])

        ret = []
        cur_level = 1
        while cur_level in rcd:
            ret.append(
                rcd[cur_level] if cur_level % 2 == 1 else 
                rcd[cur_level][::-1]
            )
            cur_level += 1
        
        return ret