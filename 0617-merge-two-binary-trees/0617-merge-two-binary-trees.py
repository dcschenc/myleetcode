# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        node1, node2 = root1, root2
        if node1 and node2:
            node = TreeNode(node1.val + node2.val)
            node.left = self.mergeTrees(node1.left, node2.left)
            node.right = self.mergeTrees(node1.right, node2.right)
        elif node1:
            node = TreeNode(node1.val)
            node.left = node1.left
            node.right = node1.right
        elif node2:
            node = TreeNode(node2.val)
            node.left = node2.left
            node.right = node2.right
        else:
            return None
        
        return node
        