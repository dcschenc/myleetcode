# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val < val:
            # return TreeNode(val, root)
            node = TreeNode(val)
            node.left = root
            return node
        root.right = self.insertIntoMaxTree(root.right, val)
        return root


        # def dfs(node, parent):
        #     if val > node.val:
        #         new_node = TreeNode(val)
        #         new_node.left = node
        #         if parent:
        #             parent.right = new_node
        #         return new_node
        #     if node.right:
        #         return dfs(node.right, node)
        #     else:
        #         node.right = TreeNode(val)
        #         return node
        # new_node = dfs(root, None)
        # if val > root.val:
        #     return new_node
        # return root    
