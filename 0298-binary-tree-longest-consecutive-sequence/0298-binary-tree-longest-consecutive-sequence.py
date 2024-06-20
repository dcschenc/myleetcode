# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            inr = 1              
            if node.left:
                left = dfs(node.left)
                if node.val + 1 == node.left.val:
                    inr = left + 1                
            if node.right:               
                right = dfs(node.right)
                if node.val + 1 == node.right.val:
                    inr = max(inr, right + 1)                
            ans[0] = max(ans[0], inr)  
            return inr

        ans = [0]
        dfs(root)
        return ans[0]
        
        def dfs(node, cur):
            ans[0] = max(ans[0], cur)            
            if node.left:
                if node.val + 1 == node.left.val:
                    dfs(node.left, cur + 1)
                else:
                    dfs(node.left, 1)
            if node.right:               
                if node.val + 1 == node.right.val:
                    dfs(node.right, cur + 1)
                else:
                    dfs(node.right, 1)            
        ans = [0]
        dfs(root, 1)
        return ans[0]

        # def dfs(node):
        #     if not node.left and not node.right:
        #         return 1
        #     left, right = 0, 0
        #     if node.left:
        #         left = dfs(node.left)
        #         if node.val + 1 == node.left.val:
        #             left += 1
        #     if node.right:
        #         right = dfs(node.right)
        #         if node.val + 1 == node.right.val:
        #             right += 1
        #     return max(left, right)

        # return dfs(root)