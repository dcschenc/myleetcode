# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        node = root
        queue = deque()
        queue.appendleft((root, 0))
        ######### BSF ############
        while queue:
            node, val = queue.pop()
            if node.left is None and node.right is None:
                res += val*10 + node.val
            if node.left:
                queue.appendleft((node.left, val*10 + node.val))
            if node.right:
                queue.appendleft((node.right, val*10 + node.val))
        return res