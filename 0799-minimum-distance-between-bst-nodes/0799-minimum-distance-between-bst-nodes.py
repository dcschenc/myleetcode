# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal mx, prev
            if node is None: return
            dfs(node.left)
            mx = min(mx, abs(node.val - prev))
            prev = node.val      
            dfs(node.right)

        mx, prev = inf, inf
        dfs(root)
        return mx

        # def inorder(node):
        #     nonlocal pre
        #     nonlocal diff           
        #     if node.left:
        #         inorder(node.left)
        #     if  pre is None:
        #         pre = node.val
        #     else:
        #         if abs(node.val-pre) < diff:
        #             diff = abs(node.val-pre)
        #         # print(diff)
        #         pre = node.val
        #     if node.right:
        #         inorder(node.right)

        # node = root
        # pre = None
        # diff = 10**5
        # inorder(node)
        # return diff