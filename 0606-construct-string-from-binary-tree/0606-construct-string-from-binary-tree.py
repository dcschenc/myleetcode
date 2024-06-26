# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(node):
            nonlocal res
            if not node:
                return
            res += str(node.val)
            if node.right or node.left:
                res += '('
                preorder(node.left)
                res += ')'
            if node.right:
                res += '('
                preorder(node.right)
                res += ')'
        res = ''
        preorder(root)    
        
        return res