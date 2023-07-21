from typing import *
from random import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        head = self.head
        ret, cnt = 0, 0

        while head != None:
            r = randint(0, cnt)
            if r == 0:
                ret = head.val

            cnt += 1
            head = head.next
    
        return ret

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()