# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #### recursive ######
        # if root.val == p.val or root.val == q.val:
        #     return root
        # if p.val < root.val < q.val or q.val < root.val < p.val:            
        #     return root
        # if root.val > p.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return self.lowestCommonAncestor(root.right, p, q)

        #### iterative ####
        node = root
        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                return node
        return None
