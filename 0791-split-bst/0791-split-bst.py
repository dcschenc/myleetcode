# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0776.Split%20BST
        def dfs(node):
            if node is None:
                return [None, None]
            if node.val <= target:
                l, r = dfs(node.right)
                node.right = l
                return [node, r]
            else:
                l, r = dfs(node.left)
                node.left = r
                return [l, node]

        return dfs(root)
