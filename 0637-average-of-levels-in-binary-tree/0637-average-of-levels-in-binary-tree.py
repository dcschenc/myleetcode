# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = deque([root])        
        while queue:            
            acc = 0
            cnt = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                acc += node.val
                cnt += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(acc/cnt)
        return res