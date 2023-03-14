from typing import *
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for idx in range(len(lists)):
            if lists[idx] is not None:
                heapq.heappush(pq,
                    (
                        lists[idx].val,
                        idx
                    )
                )
        
        fake_head = ListNode(-1)
        cur = fake_head
        while pq:
            val, idx = heapq.heappop(pq)

            cur.next = lists[idx]
            cur = cur.next
            
            if lists[idx].next is not None:
                lists[idx] = lists[idx].next
                heapq.heappush(pq,
                    (
                        lists[idx].val,
                        idx
                    )
                )
        
        return fake_head.next