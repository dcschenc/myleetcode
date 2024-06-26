# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal max_length
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left_arrow, right_arrow = 0, 0
            if node.left and node.val == node.left.val:
                left_arrow = left + 1
            if node.right and node.val == node.right.val:
                right_arrow = right + 1           
            
            max_length = max(max_length, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        max_length = 0
        dfs(root)
        return max_length