# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node):
            if not node:
                return 0           
            return max(get_height(node.left), get_height(node.right)) + 1
        
        height = get_height(root) - 1
        res = [[""] * (2**(height+1) - 1) for _ in range(height+1)]
        
        queue = deque()
        queue.append((root, 0, (2**(height+1) - 1-1)//2))
        while queue:
            for i in range(len(queue)):
                node, r, c = queue.popleft()
                res[r][c] = str(node.val)
                if node.left:
                    queue.append((node.left, r+1, c-2**(height-r-1)))
                if node.right:
                    queue.append((node.right, r+1, c+ 2**(height-r-1)))
                
        return res



