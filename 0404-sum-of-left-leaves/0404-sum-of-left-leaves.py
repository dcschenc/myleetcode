# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if not node.left and not node.right:
                if is_left:
                    return node.val
                return 0
            total = 0
            if node.left:
                total += dfs(node.left, True)
            if node.right:
                total += dfs(node.right, False)
            return total
        
        return dfs(root, False)

        # res = 0
        # def recur(node):        
        #     if node.left:
        #         if not node.left.left and not node.left.right:
        #             curr.append(node.left.val)
        #         else:
        #             recur(node.left)
        #     if node.right:
        #         recur(node.right)
        # curr = []
        # recur(root)
        # return sum(curr)

        