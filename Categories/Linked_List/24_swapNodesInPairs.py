# Definition for singly-linked list.
# class ListNode:
from typing import *

#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        fake_head = ListNode(-1)
        fake_head.next = head

        prev = fake_head
        while head and head.next:
            first, second = head, head.next
            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next

        return fake_head.next
