from typing import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def inorder(self, node):
        if node:
            self.inorder(node.left)

            if (
                not self.head and
                not self.tail
            ):
                self.head = self.tail = node
            else:
                self.tail.right = node
                node.left = self.tail
                self.tail = node

            self.inorder(node.right)


    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.head = self.tail = None
        self.inorder(root)
        if (
            self.head and
            self.tail
        ):
            self.head.left = self.tail
            self.tail.right = self.head

        return self.head
        