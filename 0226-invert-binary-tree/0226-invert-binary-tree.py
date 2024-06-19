# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        node = root
        if not node:
            return None            
        if node.left:
            self.invertTree(node.left)
        if node.right:
            self.invertTree(node.right)
        node.left, node.right = node.right, node.left
        return root