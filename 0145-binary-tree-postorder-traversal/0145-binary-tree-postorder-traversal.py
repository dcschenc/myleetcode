# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:        
#         def postorder_recursive(node):
#             if not node:
#                 return
#             if node.left:
#                 postorder_recursive(node.left)
#             if node.right:
#                 postorder_recursive(node.right)
#             res.append(node.val)
        
#         res = []
#         postorder_recursive(root)
#         return res

        res = []
        stack = []
        if root:
            stack.append((root, 'to visit'))            
        while stack:
            node, status = stack.pop()
            if status == 'visiting':
                res.append(node.val)
            else:
                stack.append((node, 'visiting'))
                if node.right:
                    stack.append((node.right, 'to visit'))
                if node.left:
                    stack.append((node.left, 'to visit'))                
        return res
            