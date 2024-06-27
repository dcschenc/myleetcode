# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0776.Split%20BST
        def dfs(node):
            if node is None:
                return [None, None]
            if node.val <= target:
                l, r = dfs(node.right)
                node.right = l
                return [node, r]
            else:
                l, r = dfs(node.left)
                node.left = r
                return [l, node]

        return dfs(root)

        # def dfs(node: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        #     if node is None:
        #         return [None, None]          
        #     # If current node's value is less than or equal to the target,
        #     # split the right subtree
        #     if node.val <= target:
        #         left_of_right, right_of_right = dfs(node.right)
        #         # Link the left part of the split right subtree to the current node's right
        #         node.right = left_of_right
        #         # The current node becomes part of the left tree, the right part
        #         # of the split right subtree becomes the right tree
        #         return [node, right_of_right]
        #     else:
        #         # If current node's value is greater than the target,
        #         # split the left subtree
        #         left_of_left, right_of_left = dfs(node.left)
        #         # Link the right part of the split left subtree to the current node's left
        #         node.left = right_of_left
        #         # The left part of the split left subtree becomes the left tree,
        #         # the current node becomes part of the right tree
        #         return [left_of_left, node]

        # # Call the helper function with the root of the BST
        # return dfs(root)

        # # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0776.Split%20BST
        # def dfs(root):
        #     if root is None:
        #         return [None, None]
        #     if root.val <= target:
        #         l, r = dfs(root.right)
        #         root.right = l
        #         return [root, r]
        #     else:
        #         l, r = dfs(root.left)
        #         root.left = r
        #         return [l, root]

        # return dfs(root)

        # def dfs(node, parent, left):
        #     if node.val == target:
        #         return node, parent, left
        #     if node.val > target:
        #         return dfs(node.left, node, True)
        #     else:
        #         return dfs(node.right, node, False)

        # if root.val == target:
        #     right = root.right
        #     root.right = None
        #     return [root, right]
        
        # node, parent, left = dfs(root, None, False)
        # if node.right:
        #     if left:
        #         parent.left = node.right
        #         node.right = None
        #     else:
        #         parent.right = node.right
        #         node.right = None
        # return [node, root]


        