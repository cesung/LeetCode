from collections import defaultdict

class DoubleLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        # two dummy nodes
        self.head, self.tail = DoubleLinkedListNode(-1, -1), DoubleLinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        self.size += 1
    
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def remove_tail(self):
        tail = self.tail.prev
        self.remove(tail)
        return tail

class LFUCache:

    def __init__(self, capacity: int):
        self.freq_to_dll = defaultdict(DoubleLinkedList)
        self.cache = {}
        self.capacity = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        return self.update(key, self.cache[key].value)

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            self.update(key, value)
        else:
            if len(self.cache) == self.capacity:
                removed_node = self.freq_to_dll[self.min_freq].remove_tail()
                del self.cache[removed_node.key]
            new_node = DoubleLinkedListNode(key, value)
            self.min_freq = 1
            self.freq_to_dll[self.min_freq].insert_head(new_node)
            self.cache[key] = new_node

    def update(self, key, value):
        node = self.cache[key]
        node.value = value
        prev_freq = node.freq
        node.freq += 1

        self.freq_to_dll[prev_freq].remove(node)
        self.freq_to_dll[node.freq].insert_head(node)

        if self.freq_to_dll[prev_freq].size == 0 and prev_freq == self.min_freq:
            self.min_freq += 1

        return node.value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
