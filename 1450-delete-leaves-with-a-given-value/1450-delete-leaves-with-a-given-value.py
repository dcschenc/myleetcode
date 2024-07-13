# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node, parent, left):
            if node.left:
                dfs(node.left, node, True)
            if node.right:
                dfs(node.right, node, False)
            if not node.left and not node.right:
                if node.val == target:
                    if parent and left:
                        parent.left = None
                    elif parent and not left:
                        parent.right = None
                    else:
                        return True
            return False

        if dfs(root, None, False):
            return None
        return root