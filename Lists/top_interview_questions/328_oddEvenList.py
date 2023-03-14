# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) time | O(1) space
    def oddEvenList(self, head: ListNode) -> ListNode:

        odd = head
        # for empty linked-list, []
        if odd is None:
            return head

        # for linked-list has only one element, [*]
        even = head.next
        if even is None:
            return head

        # the head of the even indices
        even_head = None
        prev = None

        while even is not None:
            odd.next = even.next

            if even_head is None:
                even_head = even
            else:
                prev.next = even

            prev = even
            odd = odd if odd.next is None else odd.next
            even = None if even.next is None else even.next.next

        prev.next = None
        odd.next = even_head

        return head
