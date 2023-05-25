from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverse(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            next_slow = slow.next
            slow.next = prev
            prev = slow
            slow = next_slow

        fast = slow
        slow = prev

        return
