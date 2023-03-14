from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        p, q = head, None
        
        while slow and fast and fast.next:
            print(slow.val, fast.val)
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                q = slow
                break
        
        if not q:
            return None

        while p != q:
            p = p.next
            q = q.next

        return p