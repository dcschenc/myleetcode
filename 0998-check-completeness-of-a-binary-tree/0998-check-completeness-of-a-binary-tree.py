# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        if root: queue.append(root)
        last_node = False
        while queue:            
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left and last_node == False:                    
                    queue.append(node.left)
                if node.left and last_node == True:
                    return False
                if not node.left:
                    last_node = True
                if node.right and last_node == False:
                    queue.append(node.right)       
                if node.right and last_node == True:
                    return False              
                if not node.right:
                    last_node = True
        return True