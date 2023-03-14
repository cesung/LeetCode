# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, r1, r2):
        if not r1 and not r2:
            return True

        if not r1 or not r2:
            return False

        return True if (
            r1.val == r2.val and
            self.dfs(r1.left, r2.left) and
            self.dfs(r1.right, r2.right)
        ) else False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        return self.dfs(p, q)
