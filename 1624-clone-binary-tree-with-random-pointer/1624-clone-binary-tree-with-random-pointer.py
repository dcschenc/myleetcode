# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        def dfs(node):
            if node is None:
                return None
            if node in hm:
                return hm[node]
            copy = NodeCopy(node.val)
            hm[node] = copy
            copy.left = dfs(node.left)
            copy.right = dfs(node.right)
            copy.random = dfs(node.random)
            return copy

        hm = {}
        return dfs(root)

        def dfs(node):
            if not node:
                return None
            new_node = NodeCopy(node.val)
            new_node.left = dfs(node.left)
            new_node.right = dfs(node.right)
            hm[node] = new_node
            return new_node
        
        def dfs_random(node):
            if not node:
                return
            if node.random:
                hm[node].random = hm[node.random]            
            dfs_random(node.left)
            dfs_random(node.right)
        
        hm = {}
        new_root = dfs(root)
        dfs_random(root)
        return new_root