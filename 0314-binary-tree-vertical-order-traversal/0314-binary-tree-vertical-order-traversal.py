# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, level, depth):
            hm[level].append((node.val, depth))
            if node.left:
                dfs(node.left, level - 1, depth + 1)
            if node.right:
                dfs(node.right, level + 1, depth + 1)        
        if not root: return []
        hm = defaultdict(list)
        dfs(root, 0, 0)
        keys = list(hm.keys())
        keys.sort()
        ans = []
        for k in keys:
            hm[k].sort(key=lambda x: x[1])
            ans.append([val[0] for val in hm[k]])
        return ans