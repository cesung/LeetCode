from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def reverse(self, head, tail):
        fake_head = ListNode(-1)
        fake_head.next, cur = head, head
        prev = None
        while cur != tail:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return fake_head.next

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        fake_head = ListNode(-1)
        fake_head.next = head

        cur_ptr, pos = fake_head, 0
        prev_ptr, next_ptr = None, None
        left_ptr, right_ptr = None, None

        while cur_ptr != None:
            if pos == left - 1:
                prev_ptr, left_ptr = cur_ptr, cur_ptr.next
            if pos == right:
                right_ptr, next_ptr = cur_ptr, cur_ptr.next

            cur_ptr = cur_ptr.next
            pos += 1

        cur_ptr = left_ptr
        self.reverse(cur_ptr, next_ptr)

        prev_ptr.next = right_ptr
        left_ptr.next = next_ptr

        return fake_head.next
