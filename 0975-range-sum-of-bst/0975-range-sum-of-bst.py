# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(node, res):
            if node.left:
                res = inorder(node.left, res)
            if low <= node.val <= high:
                res += node.val
            if node.val > high:
                return res
            if node.right:
                res = inorder(node.right, res)
            return res
        res = inorder(root, 0)
        return res