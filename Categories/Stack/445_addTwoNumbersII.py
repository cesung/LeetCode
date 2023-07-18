from typing import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def dfs(self, node, stk):
        if node is None:
            return

        stk.append(node.val)
        self.dfs(node.next, stk)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1, stk2 = [], []
        self.dfs(l1, stk1)
        self.dfs(l2, stk2)

        prev = None
        carry = 0
        while stk1 or stk2 or carry:
            v1 = stk1.pop() if stk1 else 0
            v2 = stk2.pop() if stk2 else 0
            val = v1 + v2 + carry
            new_node = ListNode(val % 10)
            new_node.next = prev

            carry = val // 10
            prev = new_node
        
        return prev