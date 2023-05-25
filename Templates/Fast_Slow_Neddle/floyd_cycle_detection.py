from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def cycle_detection(self, head: Optional[ListNode]) -> bool:
        has_cycle = False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                has_cycle = True
                break

        if has_cycle:
            p, q = head, slow
            while p != q:
                p = p.next
                q = q.next

        return has_cycle
