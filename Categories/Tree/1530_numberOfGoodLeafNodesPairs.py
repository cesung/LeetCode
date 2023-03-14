# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root):
        if not root:
            return []
            
        if root.left == None == root.right:
            return [1]

        left_leaves = self.dfs(root.left)
        right_leaves = self.dfs(root.right)

        for left_leaf_dist in left_leaves:
            for right_leaf_dist in right_leaves:
                if left_leaf_dist + right_leaf_dist <= self.distance:
                    self.ret += 1

        leaves = [ leaf_dist + 1 for leaf_dist in left_leaves + right_leaves]

        return leaves


    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.distance = distance
        self.ret = 0
        self.dfs(root)

        return self.ret
