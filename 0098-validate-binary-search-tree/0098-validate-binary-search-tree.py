# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_bst(node, min_val, max_val):
            if not node:
                return True
            # max_val = node.val
            if node.val >= max_val or node.val <= min_val:
                return False
            return check_bst(node.left, min_val, node.val) and check_bst(node.right, node.val, max_val)        
        
        min_val = -pow(2, 31) - 1
        max_val = pow(2, 31) + 1
        return check_bst(root, min_val, max_val)
            