# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) time | O(1) space
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head, prev, cur = None, None, None
        carry = 0

        while l1 or l2 or carry:

            sumv = carry
            sumv += 0 if l1 is None else l1.val
            sumv += 0 if l2 is None else l2.val

            cur = ListNode(sumv % 10)
            carry = sumv // 10

            if head is None:
                head = cur
            else:
                prev.next = cur

            prev = cur
            cur = cur.next

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    # O(n) time | O(1) space
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head, prev, cur = None, None, None
        carry = 0

        while l1 and l2:
            sumv = l1.val + l2.val + carry

            cur = ListNode(sumv % 10)
            carry = sumv // 10

            if head is None:
                head = cur
            else:
                prev.next = cur

            prev = cur
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sumv = l1.val + carry
            cur = ListNode(sumv % 10)
            carry = sumv // 10

            prev.next = cur

            prev = cur
            cur = cur.next
            l1 = l1.next

        while l2:
            sumv = l2.val + carry
            cur = ListNode(sumv % 10)
            carry = sumv // 10

            prev.next = cur

            prev = cur
            cur = cur.next
            l2 = l2.next

        if carry:
            cur = ListNode(carry)
            prev.next = cur

        return head

