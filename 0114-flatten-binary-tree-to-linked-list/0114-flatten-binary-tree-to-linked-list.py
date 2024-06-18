# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        stack = [root]
        while stack:
            cur_node = stack.pop()
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)

            if stack:
                cur_node.right = stack[-1]
            cur_node.left = None 

    
        # stack = []
        # node = root
        # while node:
        #     if node.left:
        #         if node.right:
        #             stack.append(node.right)
        #         node.right = node.left
        #         node.left = None
        #         node = node.right
        #     else:
        #         if node.right:
        #             node = node.right
        #         else:
        #             prev = node
        #             if len(stack) > 0:                    
        #                 node = stack.pop()
        #                 prev.right = node
        #             else:
        #                 break
                