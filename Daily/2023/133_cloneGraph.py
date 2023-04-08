from typing import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node, cloned_node):
        for neighbor in node.neighbors:
            if neighbor in self.node_mapping:
                cloned_neighbor = self.node_mapping[neighbor]
                cloned_node.neighbors.append(cloned_neighbor)
                continue
            cloned_neighbor = Node(neighbor.val)
            cloned_node.neighbors.append(cloned_neighbor)
            self.node_mapping[neighbor] = cloned_neighbor
            self.dfs(neighbor, cloned_neighbor)
    
        return

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        self.node_mapping = defaultdict(Node)
        cloned_node = Node(node.val)
        self.node_mapping[node] = cloned_node

        self.dfs(node, cloned_node)
        
        return cloned_node