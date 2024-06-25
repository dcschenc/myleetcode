# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int: 
        # https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/editorial/       
        def dfs(node):
            if not node: return [0, 0]
            inr = dcr = 1             

            if node.left:
                left = dfs(node.left)
                if node.val + 1 == node.left.val:
                    inr = left[0] + 1
                elif node.val - 1 == node.left.val:
                    dcr = left[1] + 1
            
            if node.right:               
                right = dfs(node.right)
                if node.val + 1 == node.right.val:
                    inr = max(inr, right[0] + 1)
                elif node.val - 1 == node.right.val:
                    dcr = max(dcr, right[1] + 1)

            ans[0] = max(ans[0], inr + dcr - 1)  
            return [inr, dcr]    

        ans = [0]
        dfs(root)
        return ans[0]
        