# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def dfs(node, parent):   
            if node.val == p.val:
                return (node, parent)
            if node.val > p.val:
                return dfs(node.left, node)
            return dfs(node.right, parent)                  
            
        
        node, parent = dfs(root, None)
        if not node.right:
            return parent
        node = node.right
        while node.left:
            node = node.left
        return node
        # if parent:
        #     return parent
        # else:
        #     if not node.right:
        #         return None
        #     node = node.right
        #     while node.left:
        #         node = node.left
        #     return node