# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        res = []
        inorder(root)
        return res        
        
        
        ########## iterative stack ###########
        # ans=[]
        # stack=[]
        # cur=root
        # while stack or cur:
        #     if cur:
        #         stack.append(cur)
        #         cur=cur.left
        #     else:
        #         cur=stack.pop()
        #         ans.append(cur.val)
        #         cur=cur.right
        # return ans
       
        # def dfs(curr):
        #     if curr is None:
        #         return
        #     if curr.left:
        #         dfs(curr.left)            
        #     res.append(curr.val)
        #     if curr.right:
        #         dfs(curr.right)
        # res = []
        # dfs(root)
        # return res
    
        # stack = []
#         res = []
#         node = root
#         while node:       
#             stack.append(node)
#             node = node.left
            
#         while stack:
#             node = stack.pop()
#             res.append(node.val)    
#             if node.right:               
#                 node = node.right
#                 while node:
#                     stack.append(node)     
#                     node = node.left
            
#         return res