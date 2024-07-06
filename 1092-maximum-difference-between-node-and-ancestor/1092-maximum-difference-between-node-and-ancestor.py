# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mi, mx):
            ans[0] = max(ans[0], abs(node.val - mi), abs(node.val - mx))
            mi = min(mi, node.val)
            mx = max(mx, node.val)

            if node.left:
                dfs(node.left, mi, mx)
            if node.right:
                dfs(node.right, mi, mx)

        ans = [0]
        dfs(root, root.val , root.val)
        return ans[0]
        