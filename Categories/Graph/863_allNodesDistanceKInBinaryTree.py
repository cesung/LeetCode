from typing import *
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, parent, node):
        self.node_parent[node] = parent
        if node.left is not None:
            self.dfs(node, node.left)
        if node.right is not None:
            self.dfs(node, node.right)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.node_parent = defaultdict(TreeNode)
        self.dfs(None, root)

        queue = deque( [ (target, k, None) ] )

        ret = []
        while queue:
            node, dist, prev = queue.popleft()
            if dist == 0:
                ret.append(node.val)
                continue

            for neighbor in [node.left, node.right, self.node_parent[node]]:
                if (
                    neighbor is not None and
                    neighbor is not prev
                ):
                    if dist > 0:
                        queue.append( (neighbor, dist - 1, node) )
            
        
        return ret
            
        