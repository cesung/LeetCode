from typing import *
from collections import defaultdict


class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.MOD = 499
        self.hash_table = [ListNode(-1) for _ in range(self.MOD)]

    def add(self, key: int) -> None:
        prev, _, is_exist = self.exist(key)

        if is_exist:
            return

        new_node = ListNode(key)
        prev.next = new_node

    def remove(self, key: int) -> None:
        prev, cur, is_exist = self.exist(key)
        if is_exist:
            prev.next = cur.next

    def contains(self, key: int) -> bool:
        _, _, is_exist = self.exist(key)
        return is_exist

    def exist(self, key: int) -> Tuple[Optional[ListNode], Optional[ListNode], bool]:
        hash_key = key % self.MOD
        head = self.hash_table[hash_key]

        prev, cur = head, head.next
        while cur != None:
            if cur.key == key:
                return prev, cur, True
            cur = cur.next
            prev = prev.next

        return prev, cur, False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
