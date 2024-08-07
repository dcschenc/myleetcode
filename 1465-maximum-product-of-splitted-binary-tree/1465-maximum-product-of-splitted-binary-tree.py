# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def sum(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            return root.val + sum(root.left) + sum(root.right)

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            t = root.val + dfs(root.left) + dfs(root.right)
            nonlocal ans, s
            if t < s:
                ans = max(ans, t * (s - t))
            return t

        mod = 10**9 + 7
        s = sum(root)
        ans = 0
        dfs(root)
        return ans % mod

        
        def dfs_total(node):
            total = node.val
            if node.left:
                total += dfs_total(node.left)
            if node.right:
                total += dfs_total(node.right)
            return total

        def dfs(node):            
            left, right = 0, 0
            if node.left:
                left = dfs(node.left)
                ans[0] = max(ans[0], (total - left) * left)
            if node.right:
                right = dfs(node.right)
                ans[0] = max(ans[0], (total - right) * right)
            return left + right + node.val

        ans = [0]
        total = dfs_total(root)
        dfs(root)
        return ans[0] % (10 ** 9 + 7)