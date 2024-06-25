# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return same_tree(node1.left, node2.left) and same_tree(node1.right, node2.right)
        
        node = root
        if not node and not subRoot:
            return True
        if not node or not subRoot:
            return False
        # while node:
        if same_tree(node, subRoot):
            return True
        else:
            left = self.isSubtree(node.left, subRoot)            
            right = self.isSubtree(node.right, subRoot)
            return left or right
