# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # O(1) time | O(1) space
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
