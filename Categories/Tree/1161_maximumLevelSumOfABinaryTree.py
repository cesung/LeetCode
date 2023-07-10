from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        INF = float('inf')
        queue = deque([ (root, 1) ])
        rcd = defaultdict(int)

        while queue:
            node, level = queue.popleft()
            rcd[level] += node.val
        
            if node.left is not None:
                queue.append( (node.left, level + 1) )
            if node.right is not None:
                queue.append( (node.right, level + 1) )
        
        ret = -1
        max_val = -INF
        level = 1
        while level in rcd:
            if rcd[level] > max_val:
                max_val = rcd[level]
                ret = level
            
            level += 1
            
        return ret

