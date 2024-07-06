# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            nonlocal s
            if node is None:
                return
            dfs(node.right)
            s += node.val
            node.val = s
            dfs(node.left)

        s = 0
        dfs(root)
        return root

        # def dfs(node, p):
        #     if not node.right and not node.left:
        #         node.val += p
        #         return node
        #     if node.right:
        #         prev = dfs(node.right, p)
        #         node.val += prev.val
        #     else:
        #         node.val += p
        #     if node.left:
        #         return dfs(node.left, node.val)
        #     return node

        # dfs(root, 0)
        # return root