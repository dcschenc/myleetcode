# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        visited = set()
        ans = 0
        while queue:
            ans = 0
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                ans += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return ans