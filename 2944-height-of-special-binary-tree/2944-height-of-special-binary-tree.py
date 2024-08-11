# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def heightOfTree(self, root: Optional[TreeNode]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2773.Height%20of%20Special%20Binary%20Tree
        def dfs(node: Optional[TreeNode], d: int):
            nonlocal ans
            ans = max(ans, d)
            if node.left and node.left.right != node:
                dfs(node.left, d + 1)
            if node.right and node.right.left != node:
                dfs(node.right, d + 1)

        ans = 0
        dfs(root, 0)
        return ans