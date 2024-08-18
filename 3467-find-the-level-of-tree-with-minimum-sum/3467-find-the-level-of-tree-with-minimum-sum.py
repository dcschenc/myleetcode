# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        total, level = inf, inf
        levels = 1
        while queue:
            cur = 0 
            for _ in range(len(queue)):
                node = queue.popleft()
                cur += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if cur < total:
                total, level = cur, levels
            levels += 1
        return level