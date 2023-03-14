from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, nums):
        size = len(nums)

        if size == 0:
            return None

        mid = size // 2

        root = TreeNode(nums[mid])
        root.left = self.dfs(nums[:mid])
        root.right = self.dfs(nums[mid + 1:])

        return root

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        node = head
        nums = []
        while node != None:
            nums.append(node.val)
            node = node.next

        return self.dfs(nums)