# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal mi, prev
            if node is None: return
            dfs(node.left)
            mi = min(mi, abs(node.val - prev))
            prev = node.val      
            dfs(node.right)

        mi, prev = inf, inf
        dfs(root)
        return mi
