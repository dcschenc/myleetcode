# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1448.Count%20Good%20Nodes%20in%20Binary%20Tree
        def dfs(node: TreeNode, mx: int):
            if node is None: return
            nonlocal ans
            if mx <= node.val:
                ans += 1
                mx = node.val
            dfs(node.left, mx)
            dfs(node.right, mx)

        ans = 0
        dfs(root, -1000000)
        return ans
