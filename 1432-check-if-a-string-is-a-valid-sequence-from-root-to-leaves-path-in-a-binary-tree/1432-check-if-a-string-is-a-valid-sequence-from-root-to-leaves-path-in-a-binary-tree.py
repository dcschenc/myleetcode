# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(node, idx):
            if idx == n - 1:
                return node is not None and node.val == arr[idx] and not node.left and not node.right                  

            if not node or node.val != arr[idx]:
                return False
            ans = False
            ans |= dfs(node.left, idx + 1)
            ans |= dfs(node.right, idx + 1)

            return ans

        n = len(arr)
        return dfs(root, 0)