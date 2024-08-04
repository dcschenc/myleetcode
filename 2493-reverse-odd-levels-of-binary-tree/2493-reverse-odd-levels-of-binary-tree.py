# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        levels = 0        
        while queue:
            cur = []
            for _ in range(len(queue)):
                node = queue.popleft()
                cur.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels += 1
            if levels % 2 == 0:
                left, right = 0, len(cur) - 1
                while left < right:
                    cur[left].val, cur[right].val = cur[right].val, cur[left].val
                    left +=1
                    right -= 1
        return root