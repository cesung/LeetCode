from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        INF = float('inf')
        max_twin = -INF

        left, right = head, head
        prev = None

        while right and right.next:
            right = right.next.next
            nxt_left = left.next
            left.next = prev
            prev = left
            left = nxt_left

        right = left
        left = prev

        while left and right:
            max_twin = max(
                max_twin,
                left.val + right.val
            )
            left = left.next
            right = right.next

        return max_twin
