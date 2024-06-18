# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        if root:
            queue.append(root)
        cnt = 0
        while queue:            
            cur = []
            for i in range(len(queue)):               
                node = queue.popleft()                
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if cnt % 2 == 1:
                cur.reverse()
            res.append(cur)
            cnt += 1
        return res