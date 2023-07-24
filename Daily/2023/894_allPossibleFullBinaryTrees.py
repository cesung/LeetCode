from typing import *
from collections import defaultdict

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, n: int) -> List[Optional[TreeNode]]:
        root = TreeNode(0)

        if n == 0:
            return [root]

        n -= 2
        if n in self.dp:
            return self.dp[n]

        cur = []
        for left_cnt in range(0, n + 1, 2):
            right_cnt = n - left_cnt
            for left in self.dfs(left_cnt):
                for right in self.dfs(right_cnt):
                    root.left = left
                    root.right = right
                    cur.append(copy.deepcopy(root))
                    
        self.dp[n] = cur
        return self.dp[n]
            
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
    
        self.dp = defaultdict(list)
        
        return self.dfs(n - 1)