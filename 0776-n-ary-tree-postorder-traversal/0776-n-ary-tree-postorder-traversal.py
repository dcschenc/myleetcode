"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if node:
                for child in node.children:
                    dfs(child)
                result.append(node.val)
        result = []
        dfs(root)
        return result