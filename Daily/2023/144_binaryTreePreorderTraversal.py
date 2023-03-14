# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return
        
        self.rst.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.rst = []
        self.dfs(root)
        
        return self.rst
