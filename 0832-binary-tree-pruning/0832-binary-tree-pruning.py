# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(node):
            if not node:
                return None
            # if not node.left and not node.right:
            #     if node.val == 0:
            #         return None
            #     else:
            #         return node
            if node.left:
                node.left = prune(node.left)
            if node.right:
                node.right = prune(node.right)
            if not node.left and not node.right and node.val == 0:
                return None
            return node

        root = prune(root)
        return root