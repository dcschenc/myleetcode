# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, direction, steps):   
            if node:         
                ans[0] = max(ans[0], steps)
                if direction == 'left':                   
                    dfs(node.left, 'right', steps + 1)
                    dfs(node.right, 'left', 1)
                else:                    
                    dfs(node.right, 'left', steps + 1)
                    dfs(node.left, 'right', 1)

        ans = [0]
        dfs(root, 'left', 0)
        dfs(root, 'right', 0)
        return ans[0]

        def dfs(root, l, r):
            if root is None:
                return
            nonlocal ans
            ans = max(ans, l, r)
            dfs(root.left, r + 1, 0)
            dfs(root.right, 0, l + 1)

        ans = 0
        dfs(root, 0, 0)
        return ans