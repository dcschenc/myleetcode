# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0600-0699/0662.Maximum%20Width%20of%20Binary%20Tree
        queue = deque()
        if root:
            queue.append((root, 1))
        max_width = 0
        while queue:
            first, end = -1, -1
            for i in range(len(queue)):
                node, n = queue.popleft()
                if first == -1:
                    first = n
                end = n
                if node.left:
                    queue.append((node.left, (n-1)*2 + 1))
                if node.right:
                    queue.append((node.right, n*2))
            
            max_width = max(max_width, end - first + 1)
        return max_width
                
