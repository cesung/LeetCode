from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        fake_head = ListNode()
        fake_tail = ListNode()
        
        head_ptr, tail_ptr = fake_head, fake_tail
        
        cur = head
        while cur is not None:
            if cur.val < x:
                head_ptr.next = cur
                head_ptr = head_ptr.next
            else:
                tail_ptr.next = cur
                tail_ptr = tail_ptr.next
            cur = cur.next
        
        tail_ptr.next = None
        head_ptr.next = fake_tail.next
        
        return fake_head.next