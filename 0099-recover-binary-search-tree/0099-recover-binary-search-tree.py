# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        node = root
        node1, node2, pre = None, None, None
        ### inorder travel
        while node or stack:
            if node:
                stack.append(node)
                node = node.left            
            else:
                node = stack.pop()
                if not pre:
                    pre = node
                elif node.val < pre.val:
                    if not node1:
                        node1 = pre
                        node2 = node
                    else:
                        node2 = node     
                        # break
                pre = node
                node = node.right
       
        node1.val, node2.val = node2.val, node1.val
            