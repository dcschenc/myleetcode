# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, s):
            if not node.left and not node.right:
                res.append(s)
            else:
                if node.left:
                    dfs(node.left, s + f'->{node.left.val}')
                if node.right:
                    dfs(node.right, s + f'->{node.right.val}')        
        
        res = []
        dfs(root, f'{root.val}')
        return res
