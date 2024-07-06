# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root, t):
            if root is None:
                return 0
            t = (t << 1) | root.val
            if root.left is None and root.right is None:
                return t
            return dfs(root.left, t) + dfs(root.right, t)

        return dfs(root, 0)

        # def dfs(node, path):
        #     nonlocal res
        #     if not node.left and not node.right:
        #         path = path + str(node.val)                
        #         res += int(path, 2)
        #         return
        #     if node.left:
        #         dfs(node.left, path + str(node.val))
        #     if node.right:
        #         dfs(node.right, path + str(node.val))
        # res = 0
        # dfs(root, '')
        # return res