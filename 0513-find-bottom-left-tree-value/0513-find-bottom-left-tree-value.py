# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root:
            queue.append(root)
        cur = []
        while queue:
            cur = []
            # last_row = True
            for i in range(len(queue)):
                node = queue.popleft()
                cur.append(node.val)
                if node.left:
                    # last_row = False
                    queue.append(node.left)
                if node.right:
                    # last_row = False
                    queue.append(node.right)
            if not queue:
                return cur[0]

