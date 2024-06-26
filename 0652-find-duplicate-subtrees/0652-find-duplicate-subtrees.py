# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node):
            key = str(node.val) + '('
            if node.left:
                key += dfs(node.left) 
            key += ','
            if node.right:
                key += dfs(node.right) 
            key += ')'
            hm[key].append(node)
            return key

        hm = defaultdict(list)        
        dfs(root)
        res = []
        for key in hm:
            if len(hm[key]) > 1:
                res.append(hm[key][0])
                # print(key, dict_[key])
        return res
        
