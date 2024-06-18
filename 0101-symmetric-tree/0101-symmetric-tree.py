# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.checkSymm(root.left, root.right)
    
    def checkSymm(self, left, right):
        if left and not right or not left and right:
            return False
        if not left and not right:
            return True
        if left.val != right.val:
            return False
        return self.checkSymm(left.right, right.left) and self.checkSymm(left.left, right.right)