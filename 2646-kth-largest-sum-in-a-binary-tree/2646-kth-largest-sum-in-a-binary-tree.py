# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()
        queue.append(root)
        levels = []
        while queue:
            cursum = 0
            for _ in range(len(queue)):
                cur = queue.popleft()
                cursum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                    
            levels.append(cursum)
        
        return -1 if len(levels) < k else nlargest(k, levels)[-1]
        # levels.sort(reverse=True)
        # return levels[k-1] if len(levels) >= k else -1
        