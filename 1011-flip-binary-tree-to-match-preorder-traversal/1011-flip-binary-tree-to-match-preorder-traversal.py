# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        def preorder(node, flap):
            if not node:
                return flap
            if node.val != voyage[0]: 
                return [-1]
            voyage.pop(0)
            if node.left and node.right:
                if node.left.val != voyage[0]:
                    node.left, node.right = node.right, node.left
                    flap.append(node.val)
            left = preorder(node.left, flap)
            right = preorder(node.right, flap)
            if left == [-1] or right == [-1]:
                return [-1]
            return flap
        # flap = []
        flap = preorder(root, [])
        # if res == -1:
            # return [-1]
        return flap