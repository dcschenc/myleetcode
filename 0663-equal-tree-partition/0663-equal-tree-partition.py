# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0
            l, r = dfs(root.left), dfs(root.right)
            seen.append(l + r + root.val)
            return seen[-1]

        seen = []
        s = dfs(root)
        if s % 2 == 1:
            return False
        seen.pop()
        return s // 2 in seen