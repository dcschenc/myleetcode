# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()        
        if root:
            queue.appendleft(root)
        res = []
        #######  BSF #######
        while queue:
            value = None
            for i in range(len(queue)):
                node = queue.pop()
                value = node.val
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
            res.append(value)
        return res