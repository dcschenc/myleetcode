"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # https://leetcode.com/problems/inorder-successor-in-bst-ii/editorial/
        val = node.val
        if not node.right:            
            while node.parent and node.parent.val < val:
                node = node.parent           
            return node.parent
        else:
            node = node.right
            while node.left:
                node = node.left
            return node