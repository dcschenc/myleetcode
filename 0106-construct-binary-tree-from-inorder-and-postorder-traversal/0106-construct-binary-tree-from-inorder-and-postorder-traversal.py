# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]: 
        if not inorder:
            return None
        val = postorder.pop()
        idx = inorder.index(val)
        root = TreeNode(val)
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:])
        return root

        # val = postorder[-1]

        # idx = inorder.index(val)
        # left_post = postorder[:idx]
        # right_post = postorder[idx:len(postorder)-1]        
        
        # root = TreeNode(val)
        # if idx > 0:
        #     left = self.buildTree(inorder[:idx], left_post)
        #     root.left = left
        # if idx < len(inorder)-1:
        #     right = self.buildTree(inorder[idx+1:], right_post)        
        #     root.right = right
        # return root
        
            
        