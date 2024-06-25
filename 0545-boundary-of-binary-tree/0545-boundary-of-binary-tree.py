# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:        
        def dfs_left(node):
            if not node.left and not node.right:
                return []
            left = [node.val]
            if node.left:
                left.extend(dfs_left(node.left))
            else:
                if node.right:
                    left.extend(dfs_left(node.right))
            return left

        def dfs_right(node):
            if not node.left and not node.right:
                return []
            right = [node.val]
            if node.right:
                right.extend(dfs_right(node.right))
            else:
                if node.left:
                    right.extend(dfs_right(node.left))
            return right

        def dfs_leaves(node):
            if not node.left and not node.right:
                leaves.append(node.val)
                return

            if node.left:
                dfs_leaves(node.left)
            if node.right:
                dfs_leaves(node.right)

        ans = [root.val]
        left, leaves, right = [], [], []
        if root.left:
            left = dfs_left(root.left)        
        if root.right:
            right = dfs_right(root.right)
            
        if root.left or root.right:
            dfs_leaves(root)
        right.reverse()
        ans = ans + left + leaves + right
        return ans
           