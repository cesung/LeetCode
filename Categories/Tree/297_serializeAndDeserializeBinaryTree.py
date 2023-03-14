from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def dfs(root, encoding):
            if not root:
                encoding += '#,'
            else:
                encoding += str(root.val) + ','
                encoding = dfs(root.left, encoding)
                encoding = dfs(root.right, encoding)

            return encoding
        
        encoding = ""
        return dfs(root, "")
        

    def deserialize(self, components):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def dfs(components):
            if components[0] == '#':
                components.popleft()
                return None
            
            root = TreeNode(int(components[0]))
            components.popleft()
            root.left = dfs(components)
            root.right = dfs(components)
        
            return root

        components = deque(components.split(','))
        return dfs(components)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
