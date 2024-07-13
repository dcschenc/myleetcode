# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, p, pp):
            if node:
                if pp and pp.val % 2 == 0:
                    ans[0] += node.val
            if node.left:
                dfs(node.left, node, p)
            if node.right:
                dfs(node.right, node, p)       

        ans = [0]
        dfs(root, None, None)
        return ans[0]
        