# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:

    # O(n+m) time | O(1) space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptrA, ptrB = headA, headB

        if ptrA is None or ptrB is None:
            return None

        while ptrA is not ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        return ptrA


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution2:

    def get_length(self, head):

        length = 0
        while head is not None:
            length += 1
            head = head.next

        return length

    # O(n+m) time | O(1) space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = self.get_length(headA), self.get_length(headB)
        ptrA, ptrB = headA, headB

        while lenA > lenB:
            ptrA = ptrA.next
            lenA -= 1

        while lenB > lenA:
            ptrB = ptrB.next
            lenB -= 1

        while ptrA != ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next

        return ptrA


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution3:

    # O(n+m) time | O(n+m) space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        vis = set()
        ptrA, ptrB = headA, headB

        while ptrA is not None:
            vis.add(id(ptrA))
            ptrA = ptrA.next

        while ptrB is not None:
            if id(ptrB) in vis:
                return ptrB
            else:
                vis.add(id(ptrB))
                ptrB = ptrB.next

        return None

