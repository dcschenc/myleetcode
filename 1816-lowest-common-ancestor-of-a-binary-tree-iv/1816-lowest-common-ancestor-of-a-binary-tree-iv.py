# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.parent = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/
        def dfs(node):
            if node is None or node.val in s:
                return node
            left, right = dfs(node.left), dfs(node.right)
            if left and right:
                return node
            return left or right

        s = {node.val for node in nodes}
        return dfs(root)

        # def dfs(node, parent):
        #     if not node:
        #         return
        #     if parent:
        #         hm[node] = parent
        #     if node.left:
        #         dfs(node.left, node)
        #     if node.right:
        #         dfs(node.right, node)

        # if len(nodes) == 1:
        #     return nodes[0]

        # hm = {}
        # dfs(root, None)

        # n = len(nodes)
        # parents = [[] for _ in range(n)]
        # for i, node in enumerate(nodes):
        #     parents[i].append(node)
        #     while node in hm:
        #         parents[i].append(hm[node])
        #         node = hm[node]
        #     if i > 0:
        #         parents[i] = set(parents[i])

        # for p in parents[0]:
        #     for i in range(1, n):
        #         if p not in parents[i]:
        #             break
        #         if i == n - 1:
        #             return p
        
        

        