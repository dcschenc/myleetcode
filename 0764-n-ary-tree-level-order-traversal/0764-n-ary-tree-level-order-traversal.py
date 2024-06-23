"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = deque()
        result = []
        if root:
            queue.append(root)
        while queue:
            cur = []
            for i in range(len(queue)):
                node = queue.popleft()
                cur.append(node.val)
                for child in node.children:
                    queue.append(child)
            result.append(cur)
        return result