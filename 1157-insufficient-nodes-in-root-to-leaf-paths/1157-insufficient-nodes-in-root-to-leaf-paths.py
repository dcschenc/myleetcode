# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if root is None:
            return None
        limit -= root.val
        if root.left is None and root.right is None:
            return None if limit > 0 else root
        root.left = self.sufficientSubset(root.left, limit)
        root.right = self.sufficientSubset(root.right, limit)
        return None if root.left is None and root.right is None else root
        
        def dfs(node, cur, parent, left):
            ans = False
            if not node.left and not node.right:
                if cur + node.val >= limit:  
                    ans = True
            else:            
                if node.left:
                    ans |= dfs(node.left, cur + node.val, node, True)
                if node.right:
                    ans |= dfs(node.right, cur + node.val, node, False)

            if ans == False and parent:
                if left:
                    parent.left = None
                else:
                    parent.right = None
            return ans
        
        ans = dfs(root,0, None, True)
        if ans is False:
            return None
        return root