# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.min_s = None
        self.cm = 'abcdefghijklmnopqrstuvwxyz'
        def compare(s1, s2):
            m, n = len(s1), len(s2)
            i, j = 0, 0
            while i < m and j < n:
                if s1[i] > s2[j]:
                    return s2
                elif s1[i] < s2[j]:
                    return s1
                else:
                    i += 1
                    j += 1
            if i < m:
                return s2
            return s1

        def dfs(node, s):      
            if not node:
                return
            if not node.left and not node.right:
                s = self.cm[node.val] + s
                if self.min_s is None:
                    self.min_s = s
                else:
                    self.min_s = compare(self.min_s, s)
                return 
                
            if node.left:
                dfs(node.left, self.cm[node.val] + s)    
            if node.right:
                dfs(node.right, self.cm[node.val] + s)

        dfs(root, '')
        return self.min_s