# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            get_leaf(node.left, leaves)
            get_leaf(node.right, leaves)
            return leaves
        
        leaves_1 = get_leaf(root1, [])
        leaves_2 = get_leaf(root2, [])
        return leaves_1 == leaves_2

        #     if not node.left and not node.right:
        #         return [node.val]
        #     res = []
        #     if node.left:
        #         left = get_leaf(node.left)
        #         res.extend(left)
        #     if node.right:
        #         right = get_leaf(node.right)
        #         res.extend(right)
        #     return res
        # left = get_leaf(root1)
        # right = get_leaf(root2)
        # return left == right