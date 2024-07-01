# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # https://leetcode.com/problems/distribute-coins-in-binary-tree/editorial/
        def dfs(node):
            nonlocal moves
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            moves += abs(left) + abs(right)
            return node.val + left + right - 1
        moves = 0
        dfs(root)
        return moves