# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root):
        valid_left, valid_right = True, True
        left_max, right_min = -float('inf'), float('inf')
        left_ptr, right_ptr = root.left, root.right

        if left_ptr:
            # recurive call on left-subtree
            valid_left = self.dfs(left_ptr)
            # get maximum value on left-subtree
            while left_ptr.right is not None:
                left_ptr = left_ptr.right
            left_max = left_ptr.val

        if root.right:
            # recurive call on right-subtree
            valid_right = self.dfs(right_ptr)
            # get minimum value on right-subtree
            while right_ptr.left is not None:
                right_ptr = right_ptr.left
            right_min = right_ptr.val

		# valid if and only if
		# 1. valid left-subtree
		# 2. valid right-subtree
		# 3. root value > maximum value on the left-subtree (suppose root value must > all the value in the left-subtree) and root value < minimum value on the right-subtree (suppose root value must < all the value in the right-subtree)
        return True if (valid_left and valid_right and root.val > left_max and root.val < right_min) else False


    # O(n^2) time | O(1) space
    def isValidBST(self, root):
        return self.dfs(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def __init__(self):
        self.validBST = True
        self.prev = -float('inf')

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)

        if root.val <= self.prev:
            self.validBST = False
        self.prev = root.val

        if root.right:
            self.inorder(root.right)

    # O(n) time | O(1) space
    # Inorder
    def isValidBST(self, root):
        self.inorder(root)
        return self.validBST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution3:

    def dfs(self, root, left, right):
        if root.val <= left or root.val >= right:
            return False

        left_valid, right_valid = True, True
        if root.left:
            left_valid = self.dfs(root.left, left, root.val)
        if root.right:
            right_valid = self.dfs(root.right, root.val, right)

        return left_valid and right_valid

    # O(n) time | O(1) space
    # Intervals, Boundary
    def isValidBST(self, root):
        return self.dfs(root, -float('inf'), float('inf'))
