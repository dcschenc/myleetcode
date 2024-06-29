# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            nonlocal pre 
            nonlocal head           
            if node.left:
                inorder(node.left)
            right = node.right
            if not pre:
                pre = node
                head = node
            else:                                
                pre.right = node
                pre = node
                node.left = None
                node.right = None
            if right:
                inorder(right)
            return 
        pre = None
        head = None
        inorder(root)
        return head