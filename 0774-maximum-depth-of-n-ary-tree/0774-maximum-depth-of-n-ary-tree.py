"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = deque()
        depth = 0
        if root:
            queue.append(root)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
            depth +=1
        return depth
