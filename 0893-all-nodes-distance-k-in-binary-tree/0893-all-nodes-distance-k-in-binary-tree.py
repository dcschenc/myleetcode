# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent=None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        queue = [(target, 0)]
        seen = {target}
        result = []

        while queue:
            current, distance = queue.pop(0)
            if distance == k:
                result.append(current.val)

            for candidate in [current.left, current.right, current.parent]:
                if candidate and candidate not in seen:
                    seen.add(candidate)
                    queue.append((candidate, distance + 1))

        return result