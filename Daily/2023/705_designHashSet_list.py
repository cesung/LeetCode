from typing import *
from collections import defaultdict


class MyHashSet:

    def __init__(self):
        self.MOD = 499
        self.hash_table = defaultdict(list)

    def add(self, key: int) -> None:
        hash_list = self.hash_table[key % self.MOD]

        if key in hash_list:
            return
        hash_list.append(key)

    def remove(self, key: int) -> None:
        hash_list = self.hash_table[key % self.MOD]
        try:
            hash_list.remove(key)
        except:
            pass

    def contains(self, key: int) -> bool:
        hash_list = self.hash_table[key % self.MOD]

        return True if key in hash_list else False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
