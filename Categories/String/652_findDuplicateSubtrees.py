from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def serialize(self, root):
        if not root:
            return "#,"

        encoding = str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        self.rcd[encoding] += 1
        if self.rcd[encoding] == 2:
            self.ret.append(root)

        return encoding

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.rcd = defaultdict(int)
        self.ret = []
        self.serialize(root)

        return self.ret
