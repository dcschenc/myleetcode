# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        levels = 0
        while queue:
            cur = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)                    
                cur.append(node.val)
            prev = 0
            for val in cur:
                if levels % 2 == 0:
                    if val % 2 == 0:
                        return False
                    if prev != 0 and val <= prev:
                        return False
                    prev = val
                if levels % 2 == 1:
                    if val % 2 == 1:
                        return False
                    if prev != 0 and val >= prev:
                        return False
                    prev = val            
            levels += 1
        return True
