# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, parent, depth, target):
            if not node:
                return None

            if node.val == target:
                return (parent, depth)

            left_result = dfs(node.left, node, depth + 1, target)
            right_result = dfs(node.right, node, depth + 1, target)

            return left_result or right_result

        x_info = dfs(root, None, 0, x)
        y_info = dfs(root, None, 0, y)

        return x_info[0] != y_info[0] and x_info[1] == y_info[1]


        queue = deque()
        if root:
            queue.append((root, None))
        while queue:
            x_node, y_node = None, None
            for i in range(len(queue)):
                node, parent = queue.popleft()
                if node.val == x:
                    x_node = node
                    x_parent = parent
                if node.val == y:
                    y_node = node
                    y_parent = parent
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            if x_node and y_node and x_parent != y_parent:
                return True
        return False
            