# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1973.Count%20Nodes%20Equal%20to%20Sum%20of%20Descendants
        def dfs(node):
            total = 0
            if not node.left and not node.right:
                total = 0
            else:
                if node.left:
                    total += dfs(node.left)
                if node.right:
                    total += dfs(node.right)
            if node.val == total:
                ans[0] += 1
            return total + node.val
        
        ans = [0]
        dfs(root)
        return ans[0]