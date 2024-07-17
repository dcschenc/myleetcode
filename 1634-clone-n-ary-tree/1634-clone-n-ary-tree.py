"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        def dfs(node):
            if not node:
                return None
            new_node = Node(node.val)
            new_node.children = []
            for c in node.children:
                new_c = dfs(c)
                new_node.children.append(new_c)
            return new_node

        return dfs(root)