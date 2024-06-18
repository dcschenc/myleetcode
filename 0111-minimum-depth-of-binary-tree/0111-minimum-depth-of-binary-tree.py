# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left, right = float('inf'), float('inf')
        if root.left:
            left = self.minDepth(root.left)
        if root.right:
            right = self.minDepth(root.right)
        return 1 + min(left, right)