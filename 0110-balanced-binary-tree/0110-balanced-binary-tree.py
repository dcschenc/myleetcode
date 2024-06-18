# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance_and_height(node):
            if not node:
                return True, 0

            l_balance, l_height = check_balance_and_height(node.left)
            r_balance, r_height = check_balance_and_height(node.right)

            # Check if the subtrees are balanced and calculate the height
            balanced = l_balance and r_balance and abs(l_height - r_height) <= 1
            height = max(l_height, r_height) + 1

            return balanced, height

        balanced, _ = check_balance_and_height(root)
        return balanced
