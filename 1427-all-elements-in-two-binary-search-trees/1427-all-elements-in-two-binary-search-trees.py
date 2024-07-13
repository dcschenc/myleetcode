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
        return sorted(list1 + list2)