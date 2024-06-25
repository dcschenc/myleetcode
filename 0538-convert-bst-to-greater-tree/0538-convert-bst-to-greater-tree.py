# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # https://leetcode.com/problems/convert-bst-to-greater-tree/editorial/
        total = 0        
        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        return root

        def dfs(node):
            if not node:
                return 
            nonlocal total 
            if node.right:
                dfs(node.right)
            total += node.val
            node.val = total
            if node.left:
                dfs(node.left)
        total = 0
        dfs(root)
        return root