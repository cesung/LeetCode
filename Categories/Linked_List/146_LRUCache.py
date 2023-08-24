class ListNode:
    
    def __init__(self, key: int = -1, val: int = -1) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # key -> ListNode
        self.rcd = defaultdict(ListNode)
        self.size = 0
        
        self.head = ListNode()
        self.tail = ListNode()
        
        self.head.next = self.tail 
        self.tail.prev = self.head
        
    def pop_tail(self):
        node = self.tail.prev
        del self.rcd[node.key]
        self.remove_node(node)
        
    def add_node(self, node: ListNode) -> None:
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def remove_node(self, node: ListNode) -> None:
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def move_head(self, node: ListNode) -> None:
        if not node:
            return
        self.remove_node(node)
        self.add_node(node)

    def get(self, key: int) -> int:
        node = self.rcd[key] if key in self.rcd else None
        self.move_head(node)
        
        return node.val if node else -1
        
    def put(self, key: int, value: int) -> None:
        new_node = ListNode(key, value)
        
        if key in self.rcd:
            node = self.rcd[key]
            node.val = value
            self.move_head(node)
            return
        
        if self.size == self.capacity:
            self.pop_tail()
            self.size -= 1
        
        self.size += 1
        new_node = ListNode(key, value)
        self.rcd[key] = new_node
        self.add_node(new_node)
        
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)