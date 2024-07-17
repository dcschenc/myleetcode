# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node.left and not node.right:
                ans.append(node.left.val)
            if node.right and not node.left:
                ans.append(node.right.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        ans = []
        dfs(root)
        return ans


        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left and not node.right:
                    ans.append(node.left.val)
                if node.right and not node.left:
                    ans.append(node.right.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans

