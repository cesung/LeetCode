from typing import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        size = 0
        while cur != None:
            size += 1
            cur = cur.next

        cur, idx = head, 0
        ret, stk = [0 for _ in range(size)], []
        while cur != None:
            while (
                stk and 
                stk[-1][1] < cur.val
            ):
                jdx, _ = stk.pop()
                ret[jdx] = cur.val
            
            stk.append( (idx, cur.val) )
            idx += 1

            cur = cur.next
    
        return ret