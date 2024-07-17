"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1506.Find%20Root%20of%20N-Ary%20Tree
        x = 0
        for node in tree:
            x ^= node.val
            for child in node.children:
                x ^= child.val
        return next(node for node in tree if node.val == x)    
        
        hm = set()
        for node in tree:
            for c in node.children:
                hm.add(c)
        for node in tree:
            if node not in hm:
                return node        