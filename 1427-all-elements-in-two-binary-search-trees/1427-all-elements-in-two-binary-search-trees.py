# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node, l):
            if not node:
                return
            if node.left:
                dfs(node.left, l)
            l.append(node.val)
            if node.right:
                dfs(node.right, l)

        list1, list2 = [], []
        dfs(root1, list1)
        dfs(root2, list2)
        i, j = 0, 0
        m, n = len(list1), len(list2)
        res = []
        while i < m and j < n:
            if list1[i] <= list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1
        # while i < m:
        res.extend(list1[i:])
        res.extend(list2[j:])
        return res
        
        return sorted(list1 + list2)