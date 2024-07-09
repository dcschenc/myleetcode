# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        # res = []
        max_sum = float('-inf')
        max_level = 1
        level = 1
        while queue:
            s = 0
            for i in range(len(queue)):
                node = queue.popleft()
                s += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # res.append(s)
            if s > max_sum:
                max_sum = s
                max_level = level
            level += 1
            # max_sum = max(max_sum, s)
        return max_level
        # max_s, idx = -sys.maxsize - 1, -1
        # for i in range(len(res)):
        #     if res[i] > max_s:
        #         idx = i
        #         max_s = res[i]
        # return idx+1